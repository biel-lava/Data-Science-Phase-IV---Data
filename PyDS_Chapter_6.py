'''
Chapter 6: Data Loading, Storage and File Formats
Date: 11/14/23
Reference: Python for Data Analysis (McKinney, 2022)
Topics:
    1. Reading and writing data in text format
    2. Reading text files in pieces
    3. Writing data to text format
    4. Working with other delimited formats
    5. Reading microsoft excel files
'''
# Address of trial.csv: D:\Documents\Operation UPSKILL\Python\Data Science Phase IV - Data/trial.csv


# Reading and writing data in text format

# Most basic file reading code using pandas 
#'''
import pandas as pd 

data = pd.read_csv("D:\Documents\Operation UPSKILL\Python\Data Science Phase IV - Data/trial.csv")

print(data)

#'''


# Modifying the column names

import pandas as pd

data = data = pd.read_csv("D:\Documents\Operation UPSKILL\Python\Data Science Phase IV - Data/trial2.csv")