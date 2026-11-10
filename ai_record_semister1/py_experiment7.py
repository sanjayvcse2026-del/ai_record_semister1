# Ex.No.7 - Data Cleaning and Exploratory Data Analysis using Pandas
# Single file: creates students1.csv, then cleans and analyses it.
import pandas as pd

# Create the CSV file (replaces %%writefile used in Google Colab)
csv_data = """Name,Department,Attendance,Mark
Asha,CSE,90,88
Bala,CSE,80,76
Charan,ECE,,92
Divya,ECE,95,
Eshan,CSE,85,84
"""
with open("students1.csv", "w") as f:
    f.write(csv_data)

# Choose the CSV file to analyze
filename = "students1.csv"

# Load the CSV file
df = pd.read_csv(filename)
print("--- Original Dataset ---")
print(df)
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values with column means
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Mark"] = df["Mark"].fillna(df["Mark"].mean())

# Remove duplicate records
df = df.drop_duplicates()
print("\n--- Cleaned Dataset ---")
print(df)
print("\n--- Descriptive Statistics ---")
print(df.describe())
print("\n--- Department-wise Average Marks ---")
print(df.groupby("Department")["Mark"].mean().round(2))
print("\n--- EDA Summary ---")
print("Highest Mark :", df["Mark"].max())
print("Lowest Mark :", df["Mark"].min())
print("Average Mark :", round(df["Mark"].mean(), 2))
print("Average Attendance :", round(df["Attendance"].mean(), 2))