from models.tracker import ProductivityTracker
from storage import load_tracker, save_tracker
from utils import get_task_duration, is_task_completed, get_minutes_from_hours


def main() -> None:
    tracker = load_tracker()
    print(f"Работаем с трекером за: {tracker.date}")
    

    raw_count = input("Сколько задач вы планируете добавить сегодня? ")
    try:
        count = int(raw_count)
    except ValueError:
        print("Неверный ввод, добавляем 0 задач.")
        count = 0

    for _ in range(count):
        print(f"\n--- Задача #{tracker.get_total_tasks() + 1} ---")
        duration = get_task_duration()
        completed = is_task_completed()
        tracker.add_task(duration=duration, is_completed=completed)

    hours_total = tracker.get_total_minutes() / 60.0
    hours_total_rounded = get_minutes_from_hours(hours_total)
    print(f"\n(Справка: общее время ≈ {hours_total_rounded} мин в целых часах)")


    tracker.print_report()


    save_tracker(tracker)
    print("\nДанные успешно сохранены в data/tracker.json")


if __name__ == "__main__":
    main()
