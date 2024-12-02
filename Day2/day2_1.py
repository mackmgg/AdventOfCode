import numpy as np

safe_reports = 0

# Load in the input file and go line by line
with open('input.txt') as file:
  for line in file:
    # For each line, parse the string as an array of levels and find the difference between each level
    report = np.fromstring(line, dtype=int, sep=" ")
    report_diff = np.diff(report)
    
    # If all of the levels in a report are between 1 and 3 or -1 and -3 then it is safe
    if ((report_diff >= 1).all() and (report_diff <= 3).all()) or ((report_diff >= -3).all() and (report_diff <= -1).all()):
      safe_reports += 1

print(safe_reports)