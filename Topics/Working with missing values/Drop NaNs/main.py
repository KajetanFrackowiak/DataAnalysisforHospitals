import pandas as pd


data = pd.read_csv("data/dataset/input.txt")


initial_rows = len(data)

data.dropna(inplace=True)


modified_rows = len(data)

# Print the results
print(f"{initial_rows} {modified_rows}")
