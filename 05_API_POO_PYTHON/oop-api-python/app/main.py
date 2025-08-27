# app/main.py
from fastapi import FastAPI, HTTPException
from typing import List
from .repository import InMemoryRepo
from .models import Character, Wizard, Ninja
from .schemas import CharacterCreate, CharacterOut, Message

app = FastAPI(title="OOP API – Personagens")
repo = InMemoryRepo()

@app.get("/", response_model=Message)
async def root():
    return {"message": "OOP API up!"}

@app.get("/characters", response_model=List[CharacterOut])
async def list_characters():
    return [c.to_dict() for c in repo.get_all()]

@app.post("/characters", response_model=CharacterOut, status_code=201)
async def create_character(payload: CharacterCreate):
    cid = repo.gen_id()
    if payload.type == "wizard":
        if not payload.spell:
            raise HTTPException(422, detail="'spell' é obrigatório para wizard")
        char: Character = Wizard(cid, payload.name, payload.universe, payload.spell)
    elif payload.type == "ninja":
        if not payload.technique:
            raise HTTPException(422, detail="'technique' é obrigatório para ninja")
        char = Ninja(cid, payload.name, payload.universe, payload.technique)
    else:
        raise HTTPException(400, detail="Tipo inválido")
    repo.add(char)
    return char.to_dict()

@app.get("/characters/{id}", response_model=CharacterOut)
async def get_character(id: int):
    char = repo.get(id)
    if not char:
        raise HTTPException(404, detail="Personagem não encontrado")
    return char.to_dict()

@app.delete("/characters/{id}", response_model=Message)
async def delete_character(id: int):
    ok = repo.delete(id)
    if not ok:
        raise HTTPException(404, detail="Personagem não encontrado")
    return {"message": f"Personagem {id} removido"}

@app.get("/characters/{id}/speak", response_model=Message)
async def character_speak(id: int):
    char = repo.get(id)
    if not char:
        raise HTTPException(404, detail="Personagem não encontrado")
    return {"message": char.speak()}

@app.get("/characters/type/{kind}", response_model=List[CharacterOut])
async def list_by_type(kind: str):
    kind = kind.lower()
    return [c.to_dict() for c in repo.get_all() if c.to_dict().get("type") == kind]
