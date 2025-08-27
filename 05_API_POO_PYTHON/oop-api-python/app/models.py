from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Any

class Character(ABC):
    """Classe base abstrata (polimorfismo via speak())."""
    def __init__(self, id: int, name: str, universe: str):
        self._id = id              # encapsulamento com atributo "privado" por convenção
        self._name = name
        self._universe = universe

    # Propriedades (encapsulamento/controla acesso)
    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise ValueError("Nome não pode ser vazio")
        self._name = value

    @property
    def universe(self) -> str:
        return self._universe

    @abstractmethod
    def speak(self) -> str:
        """Cada subclasse fala de um jeito (polimorfismo)."""
        raise NotImplementedError

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Representação serializável comum."""
        raise NotImplementedError

class Wizard(Character):
    def __init__(self, id: int, name: str, universe: str, spell: str):
        super().__init__(id, name, universe)
        self._spell = spell

    def speak(self) -> str:
        return f"{self.name} conjura '{self._spell}'! ✨"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": "wizard",
            "name": self.name,
            "universe": self.universe,
            "spell": self._spell,
        }

class Ninja(Character):
    def __init__(self, id: int, name: str, universe: str, technique: str):
        super().__init__(id, name, universe)
        self._technique = technique

    def speak(self) -> str:
        return f"{self.name} usa a técnica secreta '{self._technique}'. 🗡️"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": "ninja",
            "name": self.name,
            "universe": self.universe,
            "technique": self._technique,
        }