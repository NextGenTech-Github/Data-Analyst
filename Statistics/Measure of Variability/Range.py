# The difference between the largest and smallest data point in our data set is known as the range.


# Importing fractions module as fr 
# Enables to calculate harmonic_mean of a 
# set in Fraction 
from fractions import Fraction as fr 


print("Tuple of positive integer numbers")
# tuple of positive integer numbers 
data1 = (2, 3, 3, 4, 5, 5, 5, 5, 6, 6, 6, 7) 

#Finding Max 
Maximum = max(data1)
# Finding Min 
Minimum = min(data1) 
 
# Difference Of Max and Min
Range = Maximum-Minimum     
print("Maximum = {}, Minimum = {} and Range = {}".format(
    Maximum, Minimum, Range))




print("Tuple of a set of fractional numbers")
# tuple of a set of fractional numbers 
data3 = (fr(1, 2), fr(1, 2), fr(10, 3), fr(2, 3)) 

#Finding Max 
Maximum = max(data3)
# Finding Min 
Minimum = min(data3) 
 
# Difference Of Max and Min
Range = Maximum-Minimum     
print("Maximum = {}, Minimum = {} and Range = {}".format(Maximum, Minimum, Range))