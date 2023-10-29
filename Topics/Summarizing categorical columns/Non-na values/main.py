import pandas as pd

df_rock = pd.read_csv("data/dataset/input.txt")

# Use .loc to select rows where 'labels' is NaN, and then count them
non_na_count = df_rock['labels'].count()

print(non_na_count)
