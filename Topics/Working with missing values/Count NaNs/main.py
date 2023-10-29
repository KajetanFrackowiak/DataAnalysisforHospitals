#  write your code here 
import pandas as pd

data = pd.read_csv("data/dataset/input.txt")

df = pd.DataFrame(data)

missing_values = df.isna().sum()

print(missing_values)
