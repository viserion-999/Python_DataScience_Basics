import  pandas as pd
import matplotlib.pyplot as plt
from subprocess import check_output
# data frames from dictionary
country = ["Spain","France"]
population = ["11","12"]
list_label = ["country","population"]
list_col = [country,population]
zipped = list(zip(list_label,list_col))
data_dict = dict(zipped)
df = pd.DataFrame(data_dict)
print(df)

#Adding new columns
df["capital"] = ["madrid","paris"]
print(df)

# Broadcasting
df["income"] = 0 #Broadcasting entire column
print(df)

print(check_output(["ls", "../input"]).decode("utf8"))

data = pd.read_csv("../input/pokemon.csv")
data.info()

#Visual Analysis
# Plotting all data
data1 = data.loc[:,["Attack","Defense","Speed"]]
#data1.plot()
# it is confusing

#plt.show()
#so we use subplots
#data1.plot(subplots = True)
#plt.show()

# scatter plot
# data1.plot(kind = "scatter",x="Attack",y = "Defense")
# plt.show()
#
# # hist plot
# data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True)
#
# # histogram subplot with non cumulative and cumulative
# fig, axes = plt.subplots(nrows=2,ncols=1)
# data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True,ax = axes[0])
# data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True,ax = axes[1],cumulative = True)
# plt.savefig('graph.png')
# plt

#Date & Time In pandas
time_list = ["1992-03-08","1992-04-12"]
print(type(time_list[1])) # As you can see date is string
# however we want it to be datetime object
datetime_object = pd.to_datetime(time_list)
print(type(datetime_object))

#set_index() is used to make a column as index.

#RESAMPLING PANDAS TIME SERIES
# Resampling: statistical method over different time intervals
# Needs string to specify frequency like "M" = month or "A" = year
# Downsampling: reduce date time rows to slower frequency like from daily to weekly
# Upsampling: increase date time rows to faster frequency like from daily to hourly
# Interpolate: Interpolate values according to different methods like ‘linear’, ‘time’ or index’

data2.resample("A").mean()
data2.resample("M").mean()
# In real life (data is real. Not created from us like data2) we can solve this problem with interpolate
# We can interpolete from first value
data2.resample("M").first().interpolate("linear")

# Or we can interpolate with mean()
data2.resample("M").mean().interpolate("linear")

#Indexing Data Frames using Pandas
# read data
data = pd.read_csv('../input/pokemon.csv')
data= data.set_index("#")
data.head()
#Different types of data frames
data.HP[1]
data["HP"][1]
# using loc accessor
data.loc[1,["HP"]]
data[["HP","Attack"]]

#Slicing Data Frame
# Difference between selecting columns: series and dataframes
print(type(data["HP"]))     # series
print(type(data[["HP"]]))   # data frames
# Slicing and indexing series
data.loc[1:10,"HP":"Defense"]   # 10 and "Defense" are inclusive
# Reverse slicing
data.loc[10:1:-1,"HP":"Defense"]

# From something to end
data.loc[1:10,"Speed":]


#Functions to data frames:
# Plain python functions
def div(n):
    return n/2
data.HP.apply(div)

# Or we can use lambda function
data.HP.apply(lambda n : n/2)

# Defining column using other columns
data["total_power"] = data.Attack + data.Defense
data.head()

#Setting multiple indexing
data1 = data.set_index(["Type 1","Type 2"])
data1.head(100)

#pivoting data frames
dic = {"treatment":["A","A","B","B"],"gender":["F","M","F","M"],"response":[10,45,5,9],"age":[15,4,72,65]}
df = pd.DataFrame(dic)
df
# pivoting
df.pivot(index="treatment",columns = "gender",values="response")

#stacking & unstacking a dataframe
df1 = df.set_index(["treatment","gender"])
df1
df1.unstack(level=0)

# change inner and outer level index position
df2 = df1.swaplevel(0,1)
df2
#melt is opposite of stacking

#categorize/aggregate/reduce data frames

df.groupby("treatment").mean()
# we can only choose one of the feature
df.groupby("treatment").age.max()
df.groupby("treatment")[["age","response"]].min()
