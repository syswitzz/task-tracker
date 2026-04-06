from typing import Annotated

from fastapi import APIRouter, status, HTTPException, Depends

from schemas import TaskCreate, TaskResponse
import models

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db


router = APIRouter()


@router.get("", response_model=list[TaskResponse])
async def get_all_tasks():
    pass






@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_data: TaskCreate,
    db: Annotated[AsyncSession, Depends(get_db)],
):
    # check if user exists
    result = await db.execute(
        select(models.User).where(models.User.id == task_data.user_id)
    )
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    new_task = models.Task(
        title = task_data.title,
        description = task_data.description,
        completed = task_data.completed,
        user_id = task_data.user_id
    )

    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)

    return new_task
