import csv
from datetime import datetime
from pathlib import Path


INPUT = Path("data/raw/events.csv")
OUTPUT = Path("data/clean/events.csv")
EVENT_TYPES = {"click", "login", "purchase", "scroll", "view"}
FIELDS = ["user_id", "timestamp", "event_type", "duration_seconds"]


def parse_timestamp(value: str) -> datetime:
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return datetime.strptime(value, "%m/%d/%Y %H:%M:%S")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with INPUT.open(newline="") as source, OUTPUT.open("w", newline="") as target:
        reader = csv.DictReader(source)
        writer = csv.DictWriter(target, fieldnames=FIELDS)
        writer.writeheader()
        for row in reader:
            if any(not row.get(field) for field in FIELDS):
                continue
            if row["event_type"] not in EVENT_TYPES:
                continue
            try:
                duration = int(row["duration_seconds"])
                timestamp = parse_timestamp(row["timestamp"])
            except (ValueError, TypeError):
                continue
            if duration <= 0:
                continue
            writer.writerow(
                {
                    **row,
                    "timestamp": timestamp.strftime("%Y-%m-%dT%H:%M:%S"),
                    "duration_seconds": duration,
                }
            )


if __name__ == "__main__":
    main()
