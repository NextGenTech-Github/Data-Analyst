"""
Mean

Median

Mode

Median_High

Median_Low

Medial_Grouped

Variance 

Stddev: 

Corelation

Covariance

"""

# Python code to demonstrate the 
# working of mode() function 
# on a various range of data types 

# Importing the statistics module 
import statistics as st

# Importing fractions module as fr 
# Enables to calculate harmonic_mean of a 
# set in Fraction 
from fractions import Fraction as fr 

# tuple of positive integer numbers 
data1 = (2, 3, 3, 4, 5, 5, 5, 5, 6, 6, 6, 7) 

# tuple of a set of floating point values 
data2 = (2.4, 1.3, 1.3, 1.3, 2.4, 4.6) 

# tuple of a set of fractional numbers 
data3 = (fr(1, 2), fr(1, 2), fr(10, 3), fr(2, 3)) 

# tuple of a set of negative integers 
data4 = (-1, -2, -2, -2, -7, -7, -9) 

st.median_grouped(data1)

# tuple of strings 
data5 = ("red", "blue", "black", "blue", "black", "black", "brown") 

print("Data = {}, Mean={}".format(data1,st.mean(data1)))

print("Data = {}, Median={}".format(data1, st.median(data1)))

print("Data = {}, Mode={}".format(data1, st.mode(data1)))

print("Data = {}, Median_High={}".format(data1, st.median_high(data1)))

print("Data = {}, median_group={}".format(data1,st.median_grouped(data1)))

print("Data = {}, Median_low={}".format(data1,st.median_low(data1)))

print("Data = {}, Variance={}".format(data1,st.variance(data1)))

print("Data = {}, Std Deviation={}".format(data1,st.stdev(data1)))


# two parameters
print("Data = {}, correlation={}".format(data1,st.correlation(data1,data1)))

print("Data = {}, covariance={}".format(data3,st.covariance(data3,data3)))





