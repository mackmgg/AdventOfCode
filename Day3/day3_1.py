import re

# Load in imput as a string
with open('input.txt') as file:
	memory = file.read()

# Regex out all of the valid mul(X,Y) instructions
instructions = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', memory)

# For each instruction multiply the two numbers, and add it to the sum
sum = 0
for instruction in instructions:
	sum += int(instruction[0]) * int(instruction[1])

print(sum)