from models.task import Task


def test_task_creation():
    task = Task(task_id=1, duration=30, is_completed=False)
    assert task.task_id == 1
    assert task.duration == 30
    assert task.is_completed is False


def test_task_mark_completed():
    task = Task(task_id=1, duration=30, is_completed=False)
    task.mark_completed()
    assert task.is_completed is True


def test_task_str():
    task = Task(task_id=1, duration=30, is_completed=True)
    assert "Выполнена" in str(task)
    assert "30" in str(task)


def test_task_serialization():
    task = Task(task_id=2, duration=45, is_completed=True)
    data = task.to_dict()
    new_task = Task.from_dict(data)
    assert new_task.task_id == 2
    assert new_task.duration == 45
    assert new_task.is_completed is True
