import pandas as pd

df = pd.read_csv("./data/data.csv", encoding="ISO-8859-1")

# Shape
print("Rows, Columns:", df.shape)

# Column overview
print("\nColumns:\n", df.columns)

# Missing values
print("\nMissing values:\n", df.isnull().sum())

# Sample rows
print("\nSample rows:\n", df.head())

# Data types
print("\nData types:\n", df.dtypes)

# Quick stats
print("\nStats:\n", df.describe())
