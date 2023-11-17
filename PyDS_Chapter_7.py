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


# 1.a) Identifying missing data in the dataframe
'''
import pandas as pd

data = pd.read_csv("D:\Documents\Operation UPSKILL\Python\Data Science Phase IV - Data/trial4.csv" , index_col= "SN")

print(data.isna())
'''

# 1.b) Filtering out missing data 

# dropping empty rows and columns from series/ dataframes 

'''
import pandas as pd

data = pd.read_csv("D:\Documents\Operation UPSKILL\Python\Data Science Phase IV - Data/trial4.csv" , index_col= "SN")

#clean = data.dropna(axis='columns') # removes the columns that contains any null value and assigns it into a new object

clean = data.dropna() # by default yung dropna() would drop any row na may empty value


print(clean)

'''

# 1.c) Filling in missing data

'''

import pandas as pd

data = pd.read_csv("D:\Documents\Operation UPSKILL\Python\Data Science Phase IV - Data/trial4.csv" , index_col= "SN")

print(data.fillna({"Amount":100, "Section":"food"}))

'''


# DATA TRANSFORMATION

#  
'''

import pandas as pd

data = pd.read_csv("D:\Documents\Operation UPSKILL\Python\Data Science Phase IV - Data/trial4.csv" , index_col= "SN")

#print(data.duplicated()) # returns a boolean series that tells if a row is duplicated or not

print(data.drop_duplicates()) # returns the dataframe where the duplicates are removed na
'''


# 2.b) Transforming data using a function or mapping 

import pandas as pd

data = pd.read_csv("D:\Documents\Operation UPSKILL\Python\Data Science Phase IV - Data/trial4.csv" )

print(data)