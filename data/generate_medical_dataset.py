"""Generate a synthetic medical dataset relating blood pressure to age and other factors."""
from __future__ import annotations

import argparse
import csv
import math
import random
from pathlib import Path
from typing import Final, Iterable, List, Mapping

DEFAULT_ROWS: Final[int] = 50
DEFAULT_OUTPUT: Final[str] = "medical_dataset.csv"


def generate_dataset(rows: int = DEFAULT_ROWS) -> List[Mapping[str, float]]:
    """Create a dataset with a non-linear blood pressure relationship."""
    random.seed()

    records = []
    for _ in range(rows):
        age = random.randint(25, 80)
        bmi = min(max(random.gauss(27, 4.5), 18), 40)
        sodium_intake = min(max(random.gauss(3.2, 0.8), 1.5), 5.5)
        exercise_minutes = int(min(max(random.gauss(150, 40), 30), 300))
        stress_score = round(random.uniform(1, 10), 1)

        baseline = 75 + 0.7 * age + 0.4 * bmi
        modulation = 8 * math.sin(age / 12) + 4 * math.log1p(sodium_intake * 2)
        lifestyle = -0.05 * exercise_minutes + 1.8 * stress_score
        blood_pressure = baseline + modulation + lifestyle
        blood_pressure += random.gauss(0, 5.5)

        records.append(
            {
                "age": age,
                "bmi": round(bmi, 1),
                "sodium_intake_g": round(sodium_intake, 2),
                "exercise_minutes_per_week": exercise_minutes,
                "stress_score": stress_score,
                "systolic_blood_pressure": round(blood_pressure, 1),
            }
        )

    return records


def write_csv(records: Iterable[Mapping[str, float]], path: Path) -> None:
    fieldnames = [
        "age",
        "bmi",
        "sodium_intake_g",
        "exercise_minutes_per_week",
        "stress_score",
        "systolic_blood_pressure",
    ]
    with path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)


def main(rows: int, output: Path) -> None:
    dataset = generate_dataset(rows)
    write_csv(dataset, output)
    print(f"Dataset with {rows} rows written to {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-r", "--rows", type=int, default=DEFAULT_ROWS, help="Number of rows to generate",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path(DEFAULT_OUTPUT),
        help="Path to the CSV file to create",
    )
    args = parser.parse_args()
    main(args.rows, args.output)
