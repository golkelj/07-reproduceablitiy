import csv
from datetime import date
from pathlib import Path


INPUT = Path("data/transformed/events.csv")
OUTPUT = Path("data/features/events.csv")
FIELDS = [
    "user_id",
    "timestamp",
    "event_type",
    "duration_seconds",
    "date",
    "duration_minutes",
    "weekday",
]


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with INPUT.open(newline="") as source, OUTPUT.open("w", newline="") as target:
        reader = csv.DictReader(source)
        writer = csv.DictWriter(target, fieldnames=FIELDS)
        writer.writeheader()
        for row in reader:
            writer.writerow(
                {
                    **row,
                    "duration_minutes": int(row["duration_seconds"]) / 60,
                    "weekday": date.fromisoformat(row["date"]).strftime("%A"),
                }
            )


if __name__ == "__main__":
    main()
