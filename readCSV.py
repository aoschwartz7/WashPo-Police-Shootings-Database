
import numpy as np
import pandas as pd 

 
data = pd.read_csv("fatal-police-shootings-data.csv") 


# Show column headers
# for col in data.columns:
# 	print(col)

# What percentage of victims were White, Black, Asian, Native American, Hispanic?

total = len(data.index)
print(data.head())

# print(pd.count(data.loc[data['race'] == 'W']))
