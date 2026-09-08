import math 


def get_task_duration() -> int:
    raw_input: str = input("Введите длительность задачи (в минутах): ")
    duration: int = int(raw_input)  # преобразование str -> int
    return duration


def is_task_completed() -> bool:
    raw_input: str = input("Задача выполнена? (да/нет): ").strip().lower()
    return raw_input == "да"


def get_minutes_from_hours(hours: float) -> int:
    minutes: float = hours * 60.0
    return math.ceil(minutes) 


def format_minutes(total_minutes: int) -> str:
    hours: int = total_minutes // 60
    minutes: int = total_minutes % 60
    return f"{hours} ч {minutes} мин"


def calculate_completion_percent(completed: int, total: int) -> float:
    if total == 0:
        return 0.0
    ratio: float = completed / total
    percent: float = ratio * 100.0
    return percent


def get_productivity_grade(percent: float) -> str:
    if percent >= 90.0:
        grade: str = "Отлично"
    elif percent >= 70.0:
        grade = "Хорошо"
    elif percent >= 50.0:
        grade = "Удовлетворительно"
    elif percent > 0.0:
        grade = "Нужно постараться"
    else:
        grade = "День пропущен"
    return grade


def print_report(
    total_tasks: int,
    completed_tasks: int,
    total_minutes: int,
    completed_minutes: int,
    percent: float,
    grade: str,
) -> None:
    print("\n" + "=" * 40)
    print("ОТЧЁТ О ПРОДУКТИВНОСТИ ДНЯ")
    print("=" * 40)
    print(f"Всего задач:              {total_tasks}")
    print(f"Выполнено задач:          {completed_tasks}")
    print(f"Процент выполнения:       {percent:.1f}%")
    print(f"Общее время задач:        {format_minutes(total_minutes)}")
    print(f"Время выполненных задач:  {format_minutes(completed_minutes)}")
    print(f"Оценка продуктивности:    {grade}")
    print("=" * 40)


def main() -> None:

    raw_count: str = input("Сколько задач вы планируете сегодня? ")
    total_tasks: int = int(raw_count)

    completed_tasks: int = 0
    total_minutes: int = 0
    completed_minutes: int = 0

    for i in range(total_tasks):
        print(f"\n--- Задача #{i + 1} ---")
        duration: int = get_task_duration()
        completed: bool = is_task_completed()

        total_minutes += duration
        if completed:
            completed_tasks += 1
            completed_minutes += duration

    percent: float = calculate_completion_percent(completed_tasks, total_tasks)
    grade: str = get_productivity_grade(percent)

    hours_total: float = total_minutes / 60.0
    hours_total_rounded: int = get_minutes_from_hours(hours_total)
    print(f"\n(Справка: общее время ≈ {hours_total_rounded} мин в целых часах)")

    print_report(
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        total_minutes=total_minutes,
        completed_minutes=completed_minutes,
        percent=percent,
        grade=grade,
    )


if __name__ == "__main__":
    main()