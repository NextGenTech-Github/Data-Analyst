"""
It is defined as an average squared deviation from the mean. 
It is calculated by finding the difference between every data point and the average 
which is also known as the mean, squaring them, adding all of them, and then dividing by the number of data points present in our data set.

Standard Deviation
It is defined as the square root of the variance. 
It is calculated by finding the Mean, then subtracting each number from the Mean which is also 
known as the average, and squaring the result. 

"""

# Python code to demonstrate variance()
# function on varying range of data-types

import statistics as st
# importing statistics module


# importing fractions as parameter values
from fractions import Fraction as fr

# tuple of a set of positive integers
# numbers are spread apart but not very much
data1 = (1, 2, 5, 4, 8, 9, 12)

# tuple of a set of negative integers
data2 = (-2, -4, -3, -1, -5, -6)

# tuple of a set of positive and negative numbers
# data-points are spread apart considerably
data3 = (-9, -1, -0, 2, 1, 3, 4, 19)

# tuple of a set of fractional numbers
data4 = (fr(1, 2), fr(2, 3), fr(3, 4),
		fr(5, 6), fr(7, 8))

# tuple of a set of floating point values
data5 = (1.23, 1.45, 2.1, 2.2, 1.9)

# Print the variance of each samples

print("Data = {}, Variance = {}, Standard Deviation {}".format(data1, st.variance(data1), st.stdev(data1)))

print("Data = {}, Variance = {}, Standard Deviation {}".format(data2, st.variance(data2), st.stdev(data2)))

print("Data = {}, Variance = {}, Standard Deviation {}".format(data3, st.variance(data3), st.stdev(data3)))

print("Data = {}, Variance = {}, Standard Deviation {}".format(data4, st.variance(data1), st.stdev(data4)))

print("Data = {}, Variance = {}, Standard Deviation {}".format(data5, st.variance(data5), st.stdev(data5)))

