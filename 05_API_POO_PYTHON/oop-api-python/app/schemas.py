from typing import Literal, Optional
from pydantic import BaseModel, Field

CharacterType = Literal["wizard", "ninja"]

class CharacterCreate(BaseModel):
    type: CharacterType = Field(description="Tipo do personagem")
    name: str
    universe: str
    spell: Optional[str] = None   # usado se type == 'wizard'
    technique: Optional[str] = None  # usado se type == 'ninja'

class CharacterOut(BaseModel):
    id: int
    type: CharacterType
    name: str
    universe: str
    spell: Optional[str] = None
    technique: Optional[str] = None

class Message(BaseModel):
    message: str