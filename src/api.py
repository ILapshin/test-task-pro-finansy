import asyncio
from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse

import schemas
import service


router = APIRouter(
    prefix='/v1',
    tags=['API v1']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_task(request: schemas.Input):

    if request.y == 0 and request.op == '/':
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='division by zero'
        )

    # Задержка начала выполнения добавлена для симуляции долгого выполнения задачи
    task = service.calculate.apply_async(
        (
            request.x,
            request.y,
            request.op
        ),
        countdown=20
    )

    return JSONResponse({"taskId": task.id})


@router.get('/tasks/', status_code=status.HTTP_200_OK)
def get_task_list():
    return JSONResponse(service.get_task_list())


@router.get('/{task_id}/', status_code=status.HTTP_200_OK)
def get_result(task_id: str):
    return JSONResponse(service.get_task_result(task_id))
