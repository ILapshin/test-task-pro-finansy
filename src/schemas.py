from pydantic import BaseModel


class Input(BaseModel):
    x: int
    y: int
    op: str


# class TaskBase():
#     result: int


# class Task(TaskBase):
#     id: int

#     class Config():
#         from_attributes = True

