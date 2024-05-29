# Python code to demonstrate the 
# working of median() on various 
# range of data-sets 

# importing the statistics module 
import statistics as st
# from statistics import median, median_low, median_high, median_grouped 

# Importing fractions module as fr 
from fractions import Fraction as fr 

# tuple of positive integer numbers 
data1 = (2, 3, 4, 5, 7, 9, 11) 

# tuple of floating point values 
data2 = (2.4, 5.1, 6.7, 8.9) 

# tuple of fractional numbers 
data3 = (fr(1, 2), fr(44, 12), 
		fr(10, 3), fr(2, 3)) 

# tuple of a set of negative integers 
data4 = (-5, -1, -12, -19, -3) 

# tuple of set of positive 
# and negative integers 
data5 = (-1, -2, -3, -4, 4, 3, 2, 1) 


# Printing the median of above datasets 
print("Data-set " + str(data1) + " and Median is % s" % (st.median(data1))) 

print("Data-set " + str(data2) + " and Median is % s" % (st.median(data2))) 

print("Data-set " + str(data3) + " and Median is % s" % (st.median(data3))) 

print("Data-set " + str(data4) + " and Median is % s" % st.median(data4))

print("Data-set " + str(data5) + " and Median is % s" % (st.median(data5))) 


# simple list of a set of integers 
set1 = [1, 3, 3, 4, 5, 7] 
 
# Print median of the data-set 
 
# Median value may or may not 
# lie within the data-set 
print("Median of the set is % s"
    % (st.median(set1))) 
 
# Print low median of the data-set 
print("Low Median of the set is % s "
    % (st.median_low(set1)))

# Print low median of the data-set 
print("High Median of the set is % s "
    % (st.median_high(set1)))

