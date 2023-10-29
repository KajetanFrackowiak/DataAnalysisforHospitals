#  write your code here 
import pandas as pd

df = pd.read_csv("data/dataset/input.txt")

mode_totsp = df['totsp'].mode()[2]

df['totsp'] = df['totsp'].fillna(df['livingsp'] + df['nonlivingsp'])

sum_totsp = int(df['totsp'].sum())

print(sum_totsp)
