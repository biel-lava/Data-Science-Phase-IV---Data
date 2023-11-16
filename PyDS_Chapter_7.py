'''
Chapter 7: Data Cleaning and Preparation
Date: 11/16/23
Reference: Python for Data Analysis (McKinney, 2022)
Topics:
    1. Handling missing data
    2. Data transformation
    3. Extension data types
    4. String manipulation
    5. Categorical data
'''



# HANDLING MISSING DATA

import pandas as pd

data = pd.read_csv("D:\Documents\Operation UPSKILL\Python\Data Science Phase IV - Data/trial4.csv" , index_col= "SN")

print(data.isna())