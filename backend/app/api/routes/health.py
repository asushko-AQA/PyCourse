from fastapi import APIRouter

from app.core.db import db_ping

router = APIRouter()


@router.get("/health")
def health() -> dict[str, object]:
    return {"status": "ok", "db": db_ping()}
