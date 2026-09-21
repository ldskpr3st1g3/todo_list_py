from models.tracker import ProductivityTracker


def test_tracker_creation():
    tracker = ProductivityTracker(date="2023-10-25")
    assert tracker.date == "2023-10-25"
    assert tracker.get_total_tasks() == 0


def test_tracker_add_task():
    tracker = ProductivityTracker()
    task = tracker.add_task(duration=60, is_completed=True)
    assert tracker.get_total_tasks() == 1
    assert tracker.get_completed_tasks() == 1
    assert task.task_id == 1


def test_tracker_calculations():
    tracker = ProductivityTracker()
    tracker.add_task(duration=30, is_completed=True)
    tracker.add_task(duration=30, is_completed=False)
    
    assert tracker.get_total_minutes() == 60
    assert tracker.get_completed_minutes() == 30
    assert tracker.calculate_completion_percent() == 50.0
    assert tracker.get_productivity_grade() == "Удовлетворительно"


def test_tracker_serialization():
    tracker = ProductivityTracker(date="2023-10-25")
    tracker.add_task(duration=45, is_completed=True)

    data = tracker.to_dict()
    new_tracker = ProductivityTracker.from_dict(data)

    assert new_tracker.date == "2023-10-25"
    assert new_tracker.get_total_tasks() == 1
    assert new_tracker.tasks[0].duration == 45
