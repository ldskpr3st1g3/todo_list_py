class Task:

    def __init__(self, task_id: int, duration: int, is_completed: bool = False) -> None:
        self.task_id: int = task_id
        self.duration: int = duration
        self.is_completed: bool = is_completed

    def mark_completed(self) -> None:
        self.is_completed = True

    def __str__(self) -> str:
        status = "Выполнена" if self.is_completed else "Не выполнена"
        return f"Задача #{self.task_id}: {self.duration} мин ({status})"

    def to_dict(self) -> dict:
        return {
            "task_id": self.task_id,
            "duration": self.duration,
            "is_completed": self.is_completed,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(
            task_id=data["task_id"],
            duration=data["duration"],
            is_completed=data.get("is_completed", False),
        )
