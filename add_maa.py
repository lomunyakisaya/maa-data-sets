import csv
from pathlib import Path

FILE = Path("datasets/maasai/custom_maasai.csv")

HEADERS = [
    "English", "Maa", "Category",
    "Dialect", "Verified", "Source"
]

FILE.parent.mkdir(parents=True, exist_ok=True)

if not FILE.exists():
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(HEADERS)

print("\n=== MAA DATA COLLECTOR ===")

english = input("English: ").strip().lower()
maa = input("Maa: ").strip().lower()
category = input("Category: ").strip().lower()
dialect = input("Dialect: ").strip().lower()
source = input("Source: ").strip().lower()

while True:
    verified = input("Verified? (yes/no): ").strip().lower()

    if verified in ["yes", "no"]:
        break

    print("Enter only yes or no.")

if not english or not maa:
    print("Error: English and Maa cannot be empty.")
    exit()

with open(FILE, "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    if (
        row["English"].strip().lower() == english.lower()
        and row["Maa"].strip().lower() == maa.lower()
    ):
        print("Duplicate entry detected. Not saved.")
        exit()

with open(FILE, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        english, maa, category,
        dialect, verified, source
    ])

print("\nEntry saved successfully!")