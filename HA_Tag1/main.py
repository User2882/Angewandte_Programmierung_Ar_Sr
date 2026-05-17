from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import json
from pathlib import Path

#===================== Tag 1 ==============================
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

@app.get("/status")
def get_status():
    return {
        "status": "online",
        "version": "0.1.0",
        "day": 1
    }

@app.get("/about")
def get_about():
    return {
        "project": "My First API",
        "author": "Arash Sarkhab",
        "course": "Applied Programming"
    }
# ====================================== Aufgaben Tag 1 =======================================

# Aufgabe 1: Square Calculator
@app.get("/square/{n}")
def calculate_square(n: int):
    result = n * n
    return {
        "number": n,
        "square": result,
        "calculation": f"{n} × {n} = {result}"
    }


# Aufgabe 2: Student Info
@app.get("/student")
def get_student():
    return {
        "name": "Arash Sarkhab",
        "semester": 2,  
        "course": "Wirtschaftsinformatik 2.0",
        "university": "Hochschule Coburg"
    }


# Aufgabe 3: Double Calculator
@app.get("/double/{n}")
def calculate_double(n: int):
    result = n * 2
    return {
        "number": n,
        "double": result,
        "calculation": f"{n} × 2 = {result}"
    }
     
====================== Tag 2 ==============================