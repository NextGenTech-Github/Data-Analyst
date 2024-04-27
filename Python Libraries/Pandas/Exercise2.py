# 1.Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
# 2. Provide Summary information
# 3. First three rows of the data frame
# 4. Select specific columns: name,score

# Sample DataFrame:
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd

import pandas as pd
import numpy as np

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Answer 1
df = pd.DataFrame(exam_data , index=labels)
print(df)

# Answer 2
print("Summary of the basic information about this DataFrame and its data:")
print(df.info())

# Answer 3 First three rows of the data frame
print(df.iloc[:3])

# Answer 4 Selected Columns of the data frame
print("Select specific columns:")
print(df[['name', 'score']].iloc[:3])