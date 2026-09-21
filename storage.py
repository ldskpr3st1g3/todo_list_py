import json
from pathlib import Path
from models.tracker import ProductivityTracker

DEFAULT_FILE = "data/tracker.json"


def save_tracker(tracker: ProductivityTracker, filename: str = DEFAULT_FILE) -> None:
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(tracker.to_dict(), f, ensure_ascii=False, indent=2)


def load_tracker(filename: str = DEFAULT_FILE) -> ProductivityTracker:
    if not Path(filename).exists():
        return ProductivityTracker()
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return ProductivityTracker.from_dict(data)
