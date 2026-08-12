"""Progress sync endpoints (plan 08)."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import current_user, progress_service
from app.models.tables import User
from app.schemas.progress import (
    ProgressMergeRequest,
    ProgressMergeResponse,
    ProgressSnapshot,
    ProgressUpsertRequest,
    ProgressUpsertResponse,
)
from app.services.progress_service import InvalidLessonKey, ProgressService

router = APIRouter(prefix="/progress", tags=["progress"])


def _error(status_code: int, code: str, message: str) -> HTTPException:
    return HTTPException(status_code=status_code, detail={"code": code, "message": message})


@router.get("", response_model=ProgressSnapshot)
def get_progress(
    user: User = Depends(current_user),
    service: ProgressService = Depends(progress_service),
) -> ProgressSnapshot:
    return service.get_snapshot(user_id=user.id)


@router.post("", response_model=ProgressUpsertResponse)
def upsert_progress(
    payload: ProgressUpsertRequest,
    user: User = Depends(current_user),
    service: ProgressService = Depends(progress_service),
) -> ProgressUpsertResponse:
    try:
        lesson = service.upsert(user_id=user.id, payload=payload)
    except InvalidLessonKey as exc:
        raise _error(status.HTTP_404_NOT_FOUND, exc.code, str(exc)) from exc
    return ProgressUpsertResponse(lesson=lesson)


@router.post("/merge", response_model=ProgressMergeResponse)
def merge_progress(
    payload: ProgressMergeRequest,
    user: User = Depends(current_user),
    service: ProgressService = Depends(progress_service),
) -> ProgressMergeResponse:
    merged_count, snapshot = service.merge_local(
        user_id=user.id,
        lessons=payload.lessons,
        last_position=payload.last_position,
    )
    return ProgressMergeResponse(merged_count=merged_count, snapshot=snapshot)
