import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool

from subprocess import check_output
print(check_output(["ls", "../input"]).decode("utf8"))

data = pd.read_csv("../input/pokemon.csv")
#data.info()
# shape gives number of rows and columns in a tuble
#data.shape()

# info gives data type like dataframe, number of sample or row, number of feature or column, feature types and memory usage
#data.info()

#print(data['Type 1'].value_counts(dropna =False))

# For example max HP is 255 or min defense is 5
#similar to str in R
print(data.describe()) #ignore null entries

#Visual Data Analysis



data.boxplot(column='Attack',by = 'Legendary')
#plt.show()

#Melting Data

data_new = data.head()    # I only take 5 rows into new data
data_new

# id_vars = what we do not wish to melt
# value_vars = what we want to melt
melted = pd.melt(frame=data_new,id_vars = 'Name', value_vars= ['Attack','Defense'])
melted

#Pivoting Data - Reverse of Melting
melted.pivot(index = 'Name', columns = 'variable',values='value')

#Concatenating DataFrames
data1 = data.head()
data2= data.tail()
conc_data_row = pd.concat([data1,data2],axis =0,ignore_index =True) # axis = 0 : adds dataframes in row
conc_data_row


data1 = data['Attack'].head()
data2= data['Defense'].head()
conc_data_col = pd.concat([data1,data2],axis =1) # axis = 0 : adds dataframes in row
conc_data_col

#Data types:
#There are 5 basic data types: object(string),booleab, integer, float and categorical.

data.dtypes
# lets convert object(str) to categorical and int to float.
data['Type 1'] = data['Type 1'].astype('category')
data['Speed'] = data['Speed'].astype('float')

#assert statement is used to check for some expressions in data frames. It returns true/false after evaluating.
assert data["Type 2"].fillna('empty',inplace = True)
assert  data['Type 2'].notnull().all()