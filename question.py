import pandas as pd
import numpy as np

# Load the Excel file
file_path = 'C:\Drive E\Machine Learning\Lab Session Data.xlsx'

# Read the 'Purchase Data' sheet
data = pd.read_excel(file_path, sheet_name='Purchase data')

# Select columns up to 'E' (assuming columns are labeled A to E)
data_subset = data.iloc[:, :5]  # This selects the first 5 columns (0 to 4)

# Display the first few rows of the subset
print(data_subset.head())

A = data[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].values

C = data[['Payment (Rs)']].values

X = np.arange(len(data)).reshape(-1, 1)  # This creates a matrix with indices as values


print("Matrix A:")
print(A)

print("Matrix X:")
print(X)

print("\nMatrix C:")
print(C)