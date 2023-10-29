import os
import pandas as pd

# Construct the file path using os.path.join
file_path = os.path.join('data', 'dataset', 'input.txt')

# Read the data from the file
df = pd.read_csv(file_path)

# Extract the 'null_deg' column for rock "R" and mine "M" objects separately
rocks = df.loc[df.labels == 'R', 'null_deg']
mines = df.loc[df.labels == 'M', 'null_deg']

# Calculate the median of 'null_deg' column for rock "R" and mine "M" objects separately
median_R = rocks.median()
median_M = mines.median()

# Print the rounded median values
print('M = {} R = {}'.format(round(median_M, 3), round(median_R, 3)))
