from typing import Dict, List, Optional
from .models import Character

class InMemoryRepo:
    def __init__(self) -> None:
        self._data: Dict[int, Character] = {}
        self._next_id = 1

    def add(self, character: Character) -> Character:
        self._data[character.id] = character
        self._next_id = max(self._next_id, character.id + 1)
        return character

    def gen_id(self) -> int:
        nid = self._next_id
        self._next_id += 1
        return nid

    def get(self, id: int) -> Optional[Character]:
        return self._data.get(id)

    def get_all(self) -> List[Character]:
        return list(self._data.values())

    def delete(self, id: int) -> bool:
        return self._data.pop(id, None) is not None