from dataclasses import dataclass, field
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime, timezone


class TaskStatus(Enum):
    PENDING = 'PENDING'
    IN_PROGRESS = 'IN_PROGRESS'
    DONE = 'DONE'

class TaskPriority(Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

@dataclass
class Task:
    title: str
    description: str
    id: UUID = field(default_factory=uuid4)
    status: TaskStatus = field(default=TaskStatus.PENDING)
    priority: TaskPriority = field(default=TaskPriority.MEDIUM)
    created_at: datetime = field(default_factory=datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=datetime.now(timezone.utc))

    def start(self) -> None:
        if self.status != TaskStatus.PENDING:
            raise ValueError(f"Task can only be started from PENDING status, current: {self.status}")
        self.status = TaskStatus.IN_PROGRESS
        self.updated_at = datetime.now(timezone.utc)

    def complete(self) -> None:
        if self.status != TaskStatus.IN_PROGRESS:
            raise ValueError(f"Task can only be completed from IN_PROGRESS status, current: {self.status}")
        self.status = TaskStatus.DONE
        self.updated_at = datetime.now(timezone.utc)

    def is_done(self) -> bool:
        return self.status == TaskStatus.DONE

    def change_priority(self, priority: TaskPriority) -> None:
        if self.is_done():
            raise ValueError("Cannot change priority of a completed task")
        self.priority = priority
        self.updated_at = datetime.now(timezone.utc)