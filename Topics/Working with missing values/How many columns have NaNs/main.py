#  write your code here 
import pandas as pd

data = pd.read_csv("data/dataset/input.txt")

data.dropna(axis=1, inplace=True)

print(len(data.columns) - 1)
