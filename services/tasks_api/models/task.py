from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class TaskStatus(str, Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"


class Task(BaseModel):
    id: UUID
    title: str
    status: TaskStatus
    owner: str
