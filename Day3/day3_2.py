import re

# Load in imput as a string
with open('input.txt') as file:
	memory = file.read()

# Regex out all of the valid instructions
instructions = re.findall(r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)', memory)

# Parse each instruction and execute the proper function
sum = 0
enabled = True
for instruction in instructions:
	# If the instruction is do() enable the multiplier
	if instruction == 'do()':
		enabled = True
	# If the instruction is don't() disable the multiplier
	elif instruction == 'don\'t()':
		enabled = False
	# Otherwise it's probably a multiply, if the multiplier is enabled then multiply!
	elif enabled:
		numbers = instruction[4:-1].split(',')
		sum += int(numbers[0]) * int(numbers[1])

print(sum)