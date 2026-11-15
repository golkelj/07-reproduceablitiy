import csv
from pathlib import Path


INPUT = Path("data/clean/events.csv")
OUTPUT = Path("data/transformed/events.csv")
FIELDS = ["user_id", "timestamp", "event_type", "duration_seconds", "date"]


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with INPUT.open(newline="") as source, OUTPUT.open("w", newline="") as target:
        reader = csv.DictReader(source)
        writer = csv.DictWriter(target, fieldnames=FIELDS)
        writer.writeheader()
        for row in reader:
            writer.writerow({**row, "date": row["timestamp"][:10]})


if __name__ == "__main__":
    main()
