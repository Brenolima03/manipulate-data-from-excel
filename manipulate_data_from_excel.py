import pandas as pd

# Read the Excel file.
dataframe = pd.read_excel("path/file.xlsx")

# Select the column "A" or any other column (optional).
print(dataframe.columns)
column_A = dataframe["A"]

# Write the values in column "A" to a text file.
with open("new_file.txt", "w") as f:
    for value in column_A:
        print(value)
        f.write(str(value) + "\n")
