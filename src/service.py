import asyncio
from celery import Celery
from celery.result import AsyncResult

from config import redis_url


celery = Celery('celery', broker=redis_url, backend=redis_url)

@celery.task
async def calculate(x, y, op):
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y
    if op == '/':
        return x / y


def get_task_result(task_id):
    task_result = AsyncResult(id=task_id, app=celery)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return result


def get_task_list():
    i = celery.control.inspect()
    result = []

    for tasks in i.scheduled().values():
        for task in tasks:
            task_id = task['request']['id']
            result.append({
                'task_id': task_id,
                'status': AsyncResult(id=task_id, app=celery).status,
            })

    return result