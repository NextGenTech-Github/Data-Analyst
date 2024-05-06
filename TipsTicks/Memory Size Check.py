# Do you want to know how much memory an object is consuming in Python?

import sys

variableList = ['I', 'Love', 'Python'] 
variableSet = {'I', 'Love', 'Python'} 
variableTuples = ('I','Love','Python')

print(f'The memory size of a list is ' f'{sys.getsizeof(variableList)} ')
print(f'The memory size of a set is 'f'{sys.getsizeof(variableSet)} ')
print(f'The memory size of a tuple is 'f'{sys.getsizeof(variableTuples)} ')