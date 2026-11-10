# Pandas Series and DataFrame
import pandas as pd
marks = pd.Series([85, 91, 78, 88, 95],
                  index=["A", "B", "C", "D", "E"])
print("--- Pandas Series ---")
print(marks)
data = {
    "RollNo": [101, 102, 103, 104, 105],
    "Name": ["Anitha", "Bala", "Chitra", "Dinesh", "Ezhil"],
    "Department": ["CSE", "CSE", "ECE", "CSE", "ECE"],
    "Mark": [85, 91, 78, 88, 95]
}
df = pd.DataFrame(data)
print("\n--- DataFrame ---")
print(df)
print("\nAverage Mark:", round(df["Mark"].mean(), 2))
print("\nStudents scoring above 85:")
print(df[df["Mark"] > 85])