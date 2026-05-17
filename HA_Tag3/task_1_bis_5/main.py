# ========================= Hausaufgabe Tag 3 =============================

# Task 1 bis 5

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import json
from pathlib import Path
from collections import Counter
from typing import Optional

app = FastAPI(
    title="Note Taking API",
    description="Simple note management",
    version="1.0.0"
)

# Data Modelle

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[list[str]] = None


class NoteCreate(BaseModel):
    title: str
    content: str
    category: str
    tags: list[str] = []


class Note(BaseModel):
    id: int
    title: str
    content: str
    category: str
    tags: list[str] = []
    created_at: str


NOTES_FILE = Path("data/notes.json")


def load_notes():
    notes_db = []
    note_id_counter = 1

    if NOTES_FILE.exists():
        with open(NOTES_FILE, "r") as f:
            data = json.load(f)
            notes_db = [Note(**note) for note in data]

        if notes_db:
            note_id_counter = max(note.id for note in notes_db) + 1

    return notes_db, note_id_counter


def save_notes(notes_db):
    NOTES_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(NOTES_FILE, "w") as f:
        notes_data = [note.dict() for note in notes_db]
        json.dump(notes_data, f, indent=2)


# Endpunkte

@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    notes_db, note_id_counter = load_notes()

    new_note = Note(
        id=note_id_counter,
        title=note.title,
        content=note.content,
        category=note.category,
        tags=note.tags,
        created_at=datetime.now().isoformat()
    )

    notes_db.append(new_note)
    save_notes(notes_db)
    return new_note


@app.get("/notes")
def list_notes(
    category: str = None,
    search: str = None,
    tag: str = None,
    created_after: str = None,
    created_before: str = None
):
    notes_db, _ = load_notes()
    filtered = []

    for note in notes_db:
        if category and note.category != category:
            continue

        if search:
            search_lower = search.lower()
            if not (
                search_lower in note.title.lower()
                or search_lower in note.content.lower()
            ):
                continue

        if tag and tag not in note.tags:
            continue

        if created_after and note.created_at < created_after:
            continue

        if created_before and note.created_at > created_before:
            continue

        filtered.append(note)

    return filtered


@app.get("/notes/stats")
def get_note_stats():
    notes_db, _ = load_notes()

    total_notes = len(notes_db)

    by_category = {}
    for note in notes_db:
        by_category[note.category] = by_category.get(note.category, 0) + 1

    all_tags = []
    for note in notes_db:
        all_tags.extend(note.tags)

    tag_counter = Counter(all_tags)

    top_tags = []
    for tag, count in tag_counter.most_common(5):
        top_tags.append({"tag": tag, "count": count})

    return {
        "total_notes": total_notes,
        "by_category": by_category,
        "top_tags": top_tags,
        "unique_tags_count": len(tag_counter)
    }


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    notes_db, _ = load_notes()

    for note in notes_db:
        if note.id == note_id:
            return note

    raise HTTPException(status_code=404, detail="Note not found")


@app.get("/notes/category/{category}")
def get_notes_by_category(category: str):
    notes_db, _ = load_notes()
    return [note for note in notes_db if note.category == category]


@app.put("/notes/{note_id}")
def update_note(note_id: int, note_update: NoteCreate) -> Note:
    notes_db, _ = load_notes()

    for i, note in enumerate(notes_db):
        if note.id == note_id:
            updated_note = Note(
                id=note.id,
                title=note_update.title,
                content=note_update.content,
                category=note_update.category,
                tags=note_update.tags,
                created_at=note.created_at
            )
            notes_db[i] = updated_note
            save_notes(notes_db)
            return updated_note

    raise HTTPException(status_code=404, detail=f"Note with ID {note_id} not found")


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int):
    notes_db, _ = load_notes()

    for i, note in enumerate(notes_db):
        if note.id == note_id:
            notes_db.pop(i)
            save_notes(notes_db)
            return

    raise HTTPException(status_code=404, detail=f"Note with ID {note_id} not found")


@app.get("/tags")
def list_tags() -> list[str]:
    notes_db, _ = load_notes()
    all_tags = set()
    for note in notes_db:
        for tag in note.tags:
            all_tags.add(tag)
    return sorted(list(all_tags))


@app.get("/tags/{tag_name}/notes")
def get_notes_by_tag(tag_name: str) -> list[Note]:
    notes_db, _ = load_notes()
    return [note for note in notes_db if tag_name in note.tags]


@app.get("/categories")
def list_categories() -> list[str]:
    notes_db, _ = load_notes()
    categories = {note.category for note in notes_db}
    return sorted(list(categories))


@app.get("/categories/{category_name}/notes")
def get_notes_by_category_by_name(category_name: str) -> list[Note]:
    notes_db, _ = load_notes()
    return [note for note in notes_db if note.category == category_name]


@app.patch("/notes/{note_id}")
def partial_update_note(note_id: int, note_update: NoteUpdate) -> Note:
    notes_db, _ = load_notes()

    for i, note in enumerate(notes_db):
        if note.id == note_id:
            if note_update.title is not None:
                note.title = note_update.title
            if note_update.content is not None:
                note.content = note_update.content
            if note_update.category is not None:
                note.category = note_update.category
            if note_update.tags is not None:
                note.tags = note_update.tags

            notes_db[i] = note
            save_notes(notes_db)
            return note

    raise HTTPException(status_code=404, detail="Note not found")