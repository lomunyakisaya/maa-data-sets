import pandas as pd
from sklearn.model_selection import train_test_split

# Load cleaned dataset
df = pd.read_csv("datasets/maasai/maasai_clean.csv")

# First split: 80% training, 20% temporary
train, temp = train_test_split(
    df,
    test_size=0.20,
    random_state=42
)

# Second split: divide temporary into validation and testing
validation, test = train_test_split(
    temp,
    test_size=0.50,
    random_state=42
)

# Save datasets
train.to_csv("datasets/maasai/train.csv", index=False)
validation.to_csv("datasets/maasai/validation.csv", index=False)
test.to_csv("datasets/maasai/test.csv", index=False)

print("Training:", len(train))
print("Validation:", len(validation))
print("Testing:", len(test))
