import pandas as pd

FILE = "datasets/maasai/custom_maasai.csv"

df = pd.read_csv(FILE)

print("\n=== MAA DATASET REPORT ===")

print("\nTotal entries:", len(df))

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate English-Maa pairs:")
print(df.duplicated(subset=["English", "Maa"]).sum())

print("\nUnverified translations:")
print(
    (df["Verified"].str.lower() != "yes").sum()
)

print("\nEntries by category:")
print(df["Category"].value_counts())

print("\nFirst five entries:")
print(df.head().to_string(index=False))
