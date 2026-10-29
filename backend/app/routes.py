from fastapi import APIRouter, HTTPException
from .catalog import CATALOG, PREVIEW
from .schemas import BoardPreview, Catalog

router = APIRouter(prefix="/api/v1")


@router.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok", "version": "0.1.0"}


@router.get("/catalog", response_model=Catalog, tags=["playground"])
def catalog() -> Catalog:
    return CATALOG


@router.get("/games/{game_id}/preview", response_model=BoardPreview, tags=["playground"])
def game_preview(game_id: str) -> BoardPreview:
    if game_id != PREVIEW.game_id:
        raise HTTPException(status_code=404, detail="No preview is available for this game.")
    return PREVIEW
