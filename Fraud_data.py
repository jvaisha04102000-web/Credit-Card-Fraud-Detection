import pandas as pd
import numpy as np

np.random.seed(42)

n = 10000

data = pd.DataFrame({
    "amount" : np.random.normal(2000, 800, n),
    "time" : np.random.randint(0, 24, n),
    "is_international": np.random.choice([0,1], n, p=[0.85, 0.15]),
    "card_present": np.random.choice([0, 1], n, p=[0.1, 0.9]),
})

data["Class"] = (
    (data["amount"] > 5000) &
    (data["is_international"] == 1) |
    (data["card_present"] == 0) &
    (data["amount"] > 3000)
).astype(int)

data.to_csv("fraud_dataset.csv", index=False)

print("Dataset Created!")
print(data["Class"].value_counts())

