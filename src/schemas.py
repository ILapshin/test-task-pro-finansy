from pydantic import BaseModel
from typing import Literal


class Input(BaseModel):
    x: int
    y: int
    op: Literal['+','-','*','/']
