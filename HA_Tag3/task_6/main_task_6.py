# Hausaufgabe Tag 3 - task 6

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Session, create_engine, Relationship, select
from datetime import datetime
from typing import Optional, Annotated

app = FastAPI(
    title="Note Taking API",
    description="Task 6 – Database Migration",
    version="1.0.0"
)

engine = create_engine("sqlite:///notes.db")


class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)
    notes: list["Note"] = Relationship(back_populates="tags")


class Note(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    category: str
    created_at: datetime = Field(default_factory=datetime.now)
    tags: list[Tag] = Relationship(back_populates="notes")


SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


class NoteCreate(BaseModel):
    title: str
    content: str
    category: str
    tags: list[str] = []


@app.post("/notes", status_code=201)
def create_note(note: NoteCreate, session: SessionDep):
    db_note = Note(
        title=note.title,
        content=note.content,
        category=note.category
    )

    tag_objects = []
    for tag_name in set(note.tags):
        tag_name = tag_name.strip().lower()
        if not tag_name:
            continue

        existing = session.exec(
            select(Tag).where(Tag.name == tag_name)
        ).first()

        if existing:
            tag_objects.append(existing)
        else:
            new_tag = Tag(name=tag_name)
            session.add(new_tag)
            tag_objects.append(new_tag)

    db_note.tags = tag_objects
    session.add(db_note)
    session.commit()
    session.refresh(db_note)

    return {
        "id": db_note.id,
        "title": db_note.title,
        "content": db_note.content,
        "category": db_note.category,
        "tags": [t.name for t in db_note.tags],
        "created_at": db_note.created_at.isoformat()
    }


@app.get("/notes")
def list_notes(session: SessionDep):
    notes = session.exec(select(Note)).all()
    return [
        {
            "id": n.id,
            "title": n.title,
            "content": n.content,
            "category": n.category,
            "tags": [t.name for t in n.tags],
            "created_at": n.created_at.isoformat()
        }
        for n in notes
    ]


@app.get("/notes/{note_id}")
def get_note(note_id: int, session: SessionDep):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    return {
        "id": note.id,
        "title": note.title,
        "content": note.content,
        "category": note.category,
        "tags": [t.name for t in note.tags],
        "created_at": note.created_at.isoformat()
    }