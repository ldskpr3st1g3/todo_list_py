from typing import List
from .task import Task
from utils import format_minutes


class ProductivityTracker:

    def __init__(self, date: str = "Сегодня") -> None:
        self.date: str = date
        self.tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, duration: int, is_completed: bool = False) -> Task:
        task = Task(task_id=self._next_id, duration=duration, is_completed=is_completed)
        self.tasks.append(task)
        self._next_id += 1
        return task

    def get_total_tasks(self) -> int:
        return len(self.tasks)

    def get_completed_tasks(self) -> int:
        return sum(1 for t in self.tasks if t.is_completed)

    def get_total_minutes(self) -> int:
        return sum(t.duration for t in self.tasks)

    def get_completed_minutes(self) -> int:
        return sum(t.duration for t in self.tasks if t.is_completed)

    def calculate_completion_percent(self) -> float:
        total = self.get_total_tasks()
        if total == 0:
            return 0.0
        return (self.get_completed_tasks() / total) * 100.0

    def get_productivity_grade(self) -> str:
        percent = self.calculate_completion_percent()
        if percent >= 90.0:
            return "Отлично"
        if percent >= 70.0:
            return "Хорошо"
        if percent >= 50.0:
            return "Удовлетворительно"
        if percent > 0.0:
            return "Нужно постараться"
        return "День пропущен"

    def print_report(self) -> None:
         
        print("\n" + "=" * 40)
        print(f"ОТЧЁТ О ПРОДУКТИВНОСТИ ДНЯ ({self.date})")
        print("=" * 40)
        print(f"Всего задач:              {self.get_total_tasks()}")
        print(f"Выполнено задач:          {self.get_completed_tasks()}")
        print(f"Процент выполнения:       {self.calculate_completion_percent():.1f}%")
        print(f"Общее время задач:        {format_minutes(self.get_total_minutes())}")
        print(f"Время выполненных задач:  {format_minutes(self.get_completed_minutes())}")
        print(f"Оценка продуктивности:    {self.get_productivity_grade()}")
        print("=" * 40)

    def to_dict(self) -> dict:
        return {
            "date": self.date,
            "next_id": self._next_id,
            "tasks": [task.to_dict() for task in self.tasks],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "ProductivityTracker":
        tracker = cls(date=data.get("date", "Сегодня"))
        tracker._next_id = data.get("next_id", 1)
        tracker.tasks = [Task.from_dict(t_data) for t_data in data.get("tasks", [])]
        return tracker