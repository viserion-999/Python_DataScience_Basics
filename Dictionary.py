#Dictionary, Simple Logical Operations, Loops

#create dictionary and look its keys and values
#Simple Dictionary Operations

dictionary = {'spain' : 'madrid','usa' : 'vegas'}
print(dictionary.keys())
print(dictionary.values())
dictionary['spain'] = "barcelona"    # update existing entry
print(dictionary)
dictionary['france'] = "paris"       # Add new entry
print(dictionary)
del dictionary['spain']              # remove entry with key 'spain'
print(dictionary)
print('france' in dictionary)        # check include or not
dictionary.clear()                   # remove all entries in dict
print(dictionary)

import pandas as pd

data = pd.read_csv('../input/pokemon.csv')
#Series: A Series is a one-dimensional object that can hold any data type such as integers, floats and strings.
#Data frame: A DataFrame is a two dimensional object that can have columns with potential different types. Different kind of inputs include dictionaries, lists, series, and even another DataFrame.

series = data['Defense']        # data['Defense'] = series
print(type(series))
data_frame = data[['Defense']]  # data[['Defense']] = data frame
print(type(data_frame))

##
print(type(data))
x = data['Defense'] > 200
print(data[x])
import numpy as np
data[np.logical_and(data['Defense']>200, data['Attack']>100 )]
#above is same as below code
data[(data['Defense']>200) & (data['Attack']>100)]

##Loops

i = 0
while i != 5 :
    print('i is: ',i)
    i +=1
print(i,' is equal to 5')
#for loop
lis = [1,2,3,4,5]
for i in lis:
    print('i is: ',i)
print('')

#dictionary
dictionary = {'spain':'madrid','france':'paris'}
for key,value in dictionary.items():
    print(key," : ",value)
print('')

# Enumerate index and value of list
# index : value = 0:1, 1:2, 2:3, 3:4, 4:5
for index, value in enumerate(lis):
    print(index," : ",value)
print('')

# For pandas we can achieve index and value
for index,value in data[['Attack']][0:1].iterrows():
    print(index," : ",value)