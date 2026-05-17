# ========================= Hausaufgabe Tag 2 =============================
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timezone
import json
from pathlib import Path


app = FastAPI(
    title="Note Taking API",
    description="Simple note management",
    version="1.0.0"
)


# Data Modelle

class NoteCreate(BaseModel):
    title: str
    content: str
    category: str


class Note(BaseModel):
    id: int
    title: str
    content: str
    created_at: str
    category: str

# Storage


NOTES_FILE = Path("data/notes.json")


def load_notes():
    """Load notes from JSON file and return notes list and next ID counter"""
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
    """Save notes to JSON file after each change"""
    NOTES_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(NOTES_FILE, "w") as f:
        notes_data = [note.dict() for note in notes_db]
        json.dump(notes_data, f, indent=2)



# Endpunkte


@app.post("/notes", status_code=201)
def create_note(note: NoteCreate) -> Note:
    """Create a new note"""
    notes_db, note_id_counter = load_notes()

    new_note = Note(
        id=note_id_counter,
        title=note.title,
        content=note.content,
        category=note.category,  
        created_at=datetime.now().isoformat()
    )

    notes_db.append(new_note)
    save_notes(notes_db)

    return new_note


@app.get("/notes")
def list_notes() -> list[Note]:
    """Get a list of all notes"""
    notes_db, _ = load_notes()
    return notes_db

# TAsK 3

@app.get("/notes/stats")
def get_notes_stats():
    """Get statistics about notes"""

    notes_db, _ = load_notes()  

    categories = {}
    for note in notes_db:
        if note.category in categories:
            categories[note.category] += 1
        else:
            categories[note.category] = 1

    return {
        "total_notes": len(notes_db),
        "by_category": categories
    }

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    """Get a specific note by ID"""
    notes_db, _ = load_notes()

    for note in notes_db:
        if note.id == note_id:
            return note

    raise HTTPException(
        status_code=404,
        detail=f"Note with ID {note_id} not found"
    )


# TASK 2
@app.get("/notes/category/{category}")
def get_notes_by_category(category: str):
    """Get all notes in a specific category"""
    
    notes_db, _ = load_notes()  
    filtered_notes = []         

    for note in notes_db:
        if note.category == category:
            filtered_notes.append(note)

    return filtered_notes


