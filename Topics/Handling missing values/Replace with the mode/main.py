#  write your code here 

import pandas as pd

df = pd.read_csv("data/dataset/input.txt")

mode_location = df['location'].mode([0])

df['location'].fillna(mode_location, inplace=True)

print(df.head(5))
