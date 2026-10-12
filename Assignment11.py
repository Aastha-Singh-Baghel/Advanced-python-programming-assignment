import pandas as pd
import numpy as np

# Create a Series containing 10 random numbers
series = pd.Series(np.random.randint(1, 100, 10))

print("Original Series:")
print(series)

# Indexing
print("\nElement at index 3:", series[3])

# Filtering
print("\nNumbers greater than 50:")
print(series[series > 50])

# Statistical operations
print("\nMean:", series.mean())
print("Median:", series.median())
print("Minimum:", series.min())
print("Maximum:", series.max())