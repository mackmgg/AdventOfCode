import numpy as np

safe_reports = 0

def check_report(report):
  # Check if difference between levels in report are all between 1 and 3 or -1 and -3
  report_diff = np.diff(report)
  if ((report_diff >= 1).all() and (report_diff <= 3).all()) or ((report_diff >= -3).all() and (report_diff <= -1).all()):
    return True
  else:
    return False

# Load in the input file and go line by line
with open('input.txt') as file:
  for line in file:
    # For each line, parse the string as an array of levels and check if safe
    report = np.fromstring(line, dtype=int, sep=" ")
    if check_report(report):
      safe_reports += 1
    else:
      # If it's not safe, iterate through removing one level and check if it is now safe
      for i in range(len(report)):
        mask = np.ones(len(report), dtype=bool)
        mask[i] = False
        
        # If it's safe with one skipped level, count that and move on to the next report
        if check_report(report[mask]):
          safe_reports += 1
          break

print(safe_reports)