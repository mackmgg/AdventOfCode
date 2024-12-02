import pandas as pd
import numpy as np

# Read in my input and separate into left and right
locations = pd.read_csv('input.txt', sep='   ', names=['Left','Right'])

similarity = 0

# Create a dataframe with the number of times each value occurs in the right list
right_location_counts = locations['Right'].value_counts()

# For each value in the left list, multiply the value by the number of times it occurs in the right list and add that to the similarity score.
# If the value doesn't occur in the right list this causes a KeyError, which can be ignored since nothing should be added to the final score.
for location in locations['Left']:
  try:
    similarity += location * right_location_counts[location]
  except KeyError:
    pass

print(similarity)
