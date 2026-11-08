import pandas as pd

# Load original dataset
df = pd.read_csv("datasets/maasai/maasai_dataset.csv")

print("Original rows:", len(df))

# Remove rows with missing translations
df = df.dropna(subset=["English", "Masaai"])

# Remove leading and trailing whitespace
df["English"] = df["English"].str.strip()
df["Masaai"] = df["Masaai"].str.strip()

# Remove empty translations
df = df[
    (df["English"] != "") &
    (df["Masaai"] != "")
]

# Remove duplicate sentence pairs
df = df.drop_duplicates(subset=["English", "Masaai"])

# Save cleaned dataset
df.to_csv(
    "datasets/maasai/maasai_clean.csv",
    index=False
)

print("Cleaned rows:", len(df))
print("Removed rows:", 31102 - len(df))
print("Saved: datasets/maasai/maasai_clean.csv")
