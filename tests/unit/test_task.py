import pytest
from task_manager.domain.model.task import Task, TaskStatus, TaskPriority


class TestTask:

    def test_task_is_created_with_pending_status(self):
        task = Task(title="Fix bug", description="Fix login bug")

        assert task.status == TaskStatus.PENDING

    def test_task_is_created_with_medium_priority(self):
        task = Task(title="Fix bug", description="Fix login bug")

        assert task.priority == TaskPriority.MEDIUM

    def test_task_has_unique_id(self):
        task1 = Task(title="Task 1", description="Description 1")
        task2 = Task(title="Task 2", description="Description 2")

        assert task1.id != task2.id

    def test_task_start_changes_status_to_in_progress(self):
        task = Task(title="Fix bug", description="Fix login bug")

        task.start()

        assert task.status == TaskStatus.IN_PROGRESS

    def test_task_complete_changes_status_to_done(self):
        task = Task(title="Fix bug", description="Fix login bug")
        task.start()

        task.complete()

        assert task.status == TaskStatus.DONE

    def test_task_cannot_start_if_already_in_progress(self):
        task = Task(title="Fix bug", description="Fix login bug")
        task.start()

        with pytest.raises(ValueError):
            task.start()

    def test_task_cannot_complete_if_pending(self):
        task = Task(title="Fix bug", description="Fix login bug")

        with pytest.raises(ValueError):
            task.complete()

    def test_task_cannot_change_priority_when_done(self):
        task = Task(title="Fix bug", description="Fix login bug")
        task.start()
        task.complete()

        with pytest.raises(ValueError):
            task.change_priority(TaskPriority.HIGH)

    def test_task_change_priority(self):
        task = Task(title="Fix bug", description="Fix login bug")

        task.change_priority(TaskPriority.HIGH)

        assert task.priority == TaskPriority.HIGH
