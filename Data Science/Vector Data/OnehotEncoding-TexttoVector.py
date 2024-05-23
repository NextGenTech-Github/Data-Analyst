# pip install pandas sklearn numpy

import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

data = {'feature1': ['A', 'B', 'C'], 'feature2': [1, 2, 3]}
df = pd.DataFrame(data)

# One-hot encoding
encoder = OneHotEncoder()
encoded_features = encoder.fit_transform(df[['feature1']]).toarray()
numerical_features = df[['feature2']].values
vectors = np.hstack([encoded_features, numerical_features])

print(vectors)
