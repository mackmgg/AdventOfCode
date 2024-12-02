import pandas as pd
import numpy as np

# Read in my input and separate into left and right
locations = pd.read_csv('input.txt', sep='   ', names=['Left','Right'])

# Sort both columns
sorted_locations = locations.transform(np.sort)

# Find difference between left and right columns
sorted_locations['Distance'] = np.abs(sorted_locations['Left'] - sorted_locations['Right'])

# Total of this difference is the answer
print(sorted_locations['Distance'].sum())
