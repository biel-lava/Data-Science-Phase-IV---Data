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
'''
import pandas as pd 

data = pd.read_csv("D:\Documents\Operation UPSKILL\Python\Data Science Phase IV - Data/trial.csv")

print(data)

'''


# Modifying the column names into custom column names defined by the user
'''
import pandas as pd

data = pd.read_csv("D:\Documents\Operation UPSKILL\Python\Data Science Phase IV - Data/trial2.csv", names=["Date", "Amount", "Column"])

print(data)
'''


# Making custom index for the rows 
'''
import pandas as pd

data = pd.read_csv("D:\Documents\Operation UPSKILL\Python\Data Science Phase IV - Data/trial3.csv" , index_col= "SN")

print(data)

'''


# Checking for empty cells in the file

'''
import pandas as pd

#data = pd.read_csv("D:\Documents\Operation UPSKILL\Python\Data Science Phase IV - Data/trial4.csv" , index_col= "SN") # blank cells will show as NaN
data = pd.read_csv("D:\Documents\Operation UPSKILL\Python\Data Science Phase IV - Data/trial4.csv" , index_col= "SN", na_values=["food"]) # yung list sa na_values will be the values sa files na icoconsider as "missing" hence yung lalabas sa dataframe ay NaN

print(data) # upon printing the dataframe the blank cells will show "NaN"

'''

# Selecting certain rows from a large dataset
'''
import pandas as pd

data = pd.read_csv("D:\Documents\Operation UPSKILL\Python\Data Science Phase IV - Data/trial5.csv", nrows=10)

print(data)
'''

# Writing data into into a separate csv file

import pandas as pd 

data = pd.read_csv("D:\Documents\Operation UPSKILL\Python\Data Science Phase IV - Data/trial5.csv", nrows=10)

data.to_csv("D:\Documents\Operation UPSKILL\Python\Data Science Phase IV - Data/trial6.csv")

