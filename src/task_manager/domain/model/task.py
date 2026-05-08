from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TaskPriority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class Task:
    title: str
    description: str
    id: UUID = field(default_factory=uuid4)
    status: TaskStatus = field(default=TaskStatus.PENDING)
    priority: TaskPriority = field(default=TaskPriority.MEDIUM)
    created_at: datetime = field(default_factory=utcnow)
    updated_at: datetime = field(default_factory=utcnow)

    def start(self) -> None:
        if self.status != TaskStatus.PENDING:
            raise ValueError(f"Task can only be started from PENDING status, current: {self.status}")
        self.status = TaskStatus.IN_PROGRESS
        self.updated_at = utcnow()

    def complete(self) -> None:
        if self.status != TaskStatus.IN_PROGRESS:
            raise ValueError(f"Task can only be completed from IN_PROGRESS status, current: {self.status}")
        self.status = TaskStatus.DONE
        self.updated_at = utcnow()

    def is_done(self) -> bool:
        return self.status == TaskStatus.DONE

    def change_priority(self, priority: TaskPriority) -> None:
        if self.is_done():
            raise ValueError("Cannot change priority of a completed task")
        self.priority = priority
        self.updated_at = utcnow()
