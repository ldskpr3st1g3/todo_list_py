import math


def get_task_duration() -> int:
    while True:
        try:
            raw_input = input("Введите длительность задачи (в минутах): ")
            return int(raw_input)
        except ValueError:
            print("Ошибка: введите целое число.")


def is_task_completed() -> bool:
    raw_input = input("Задача выполнена? (да/нет): ").strip().lower()
    return raw_input == "да"


def format_minutes(total_minutes: int) -> str:
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours} ч {minutes} мин"


def get_minutes_from_hours(hours: float) -> int:
    minutes: float = hours * 60.0
    return math.ceil(minutes)
