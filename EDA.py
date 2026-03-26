import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("fraud_dataset.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())

sns.countplot(x="Class", data=df)
plt.title("Fraud vs Normal Transactions")
plt.show()

sns.boxplot(x="Class", y="amount", data=df)
plt.show()

sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()

sns.countplot(x="is_international", hue="class", data=df)
plt.show()

