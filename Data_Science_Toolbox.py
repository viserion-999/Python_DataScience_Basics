#Content:
#
# 1. scope
# 2. Functions
# 3. Argument types
# 4. Lambda Functions
# 5. Iterations
# 6. Zip/Unzip lists
# 7.


#tuple are user defined objects which are immutable

#Scope

# What we need to know about scope:
#
# global: defined main body in script
# local: defined in a function
# built in scope: names in predefined built in scope module such as print, len

x = 5
def f():
    y = 2*x        # there is no local scope x
    return y
print(f())         # it uses global scope x
# First local scopesearched, then global scope searched, if two of them cannot be found lastly built in scope searched.

#Built in Scope
import builtins
dir(builtins)

#Nested Functions
#nested function
def square():
    """ return square of value """
    def add():
        """ add two local variable """
        x = 2
        y = 3
        z = x + y
        return z
    return add()**2
print(square())

#First checks local scope, else global scope if not then built inscope

#Argument types:
#1. Default
#2. Flexible Args
#3. Dictionary
#4. Lambda Functins
#5. Iterators

# flexible arguments *args
def f(*args):
    for i in args:
        print(i)
f(1)
print("")
f(1,2,3,4)
# flexible arguments **kwargs that is dictionary
def f(**kwargs):
    """ print key and value of dictionary"""
    for key, value in kwargs.items():               # If you do not understand this part turn for loop part and look at dictionary in for loop
        print(key, " ", value)
f(country = 'spain', capital = 'madrid', population = 123456)


# Lambda Functions:
#https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/

#
# iterable is an object that can return an iterator
# iterable: an object with an associated iter() method
# example: list, strings and dictionaries
# iterator: produces next value with next() method
#Harika told use Generators instead of iterators
# iteration example
name = "ronaldo"
it = iter(name)
print(next(it))    # print next iteration
print(*it)         # print remaining iteration


# zip example
list1 = [1,2,3,4]
list2 = [5,6,7,8]
z = zip(list1,list2)
print(z)
z_list = list(z)
print(z_list)
#unzip example
un_zip = zip(*z_list)
un_list1,un_list2 = un_zip(un_zip) # unzip returns tuble
print(un_list1)
print(un_list2)
print(type(un_list2))