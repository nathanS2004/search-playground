from typing import Literal
from pydantic import BaseModel


class CatalogEntry(BaseModel):
    id: str
    name: str
    description: str
    implemented: bool = False


class GameEntry(CatalogEntry):
    preview_available: bool = False


class Catalog(BaseModel):
    games: list[GameEntry]
    algorithms: list[CatalogEntry]
    heuristics: list[CatalogEntry]


class BoardPreview(BaseModel):
    game_id: str
    size: int
    tiles: list[int]
    goal: list[int]
    interactive: Literal[False] = False
