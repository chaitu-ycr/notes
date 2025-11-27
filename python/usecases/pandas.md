# 🐼 Usecase: Data Analysis with `pandas`

If you're going to do any kind of data analysis or data science in Python, **pandas** is the first tool you'll reach for. It is the undisputed king of data manipulation in Python, providing fast, flexible, and expressive data structures designed to make working with structured ("tabular") data like spreadsheets or SQL tables intuitive and easy.

---

## 🎯 Pandas: Practical, Tricky, and Fun Usages

```python
# ===== 1. Install pandas =====
# pip install pandas

# ===== 2. Create DataFrame from CSV =====
import pandas as pd
csv_data = """Name,Age,City\nAlice,25,NY\nBob,30,LA\nCharlie,22,Chicago\n"""
with open("people.csv", "w") as f:
    f.write(csv_data)
df = pd.read_csv("people.csv")

# ===== 3. Inspect Data =====
print(df.head())
print(df.info())
print(df.describe())

# ===== 4. Select Columns =====
names = df["Name"]
print(names)
subset = df[["Name", "City"]]
print(subset)

# ===== 5. Filter Rows =====
over_25 = df[df["Age"] > 25]
print(over_25)

# ===== 6. Group and Aggregate =====
avg_age = df.groupby("City")["Age"].mean()
print(avg_age)

# ===== 7. Add New Column =====
df["Over_30"] = df["Age"] > 30
print(df)

# ===== 8. Fun: Sorting =====
print(df.sort_values("Age", ascending=False))

# ===== 9. Fun: Missing Data =====
df.loc[1, "Age"] = None
print(df.isnull().sum())
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)

# ===== 10. Fun: Plotting =====
import matplotlib.pyplot as plt
df.plot(x="Name", y="Age", kind="bar")
plt.show()

# ===== 11. Export to Excel =====
df.to_excel("people.xlsx", index=False)

# ===== 12. Pro-Tips =====
# Use .loc and .iloc for advanced selection
# Use .apply for custom functions
# Use .merge for joining DataFrames
```
