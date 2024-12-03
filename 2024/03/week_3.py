import re

def problem_1():
	with open('input.txt') as dataset:
		total = 0
		for line in dataset:
			multiply_instructions = re.findall('mul\(\d{1,3},\d{1,3}\)',line)
			for instruction in multiply_instructions:
				numbers = [int(x) for x in instruction[4:-1].split(',')]
				total += numbers[0] * numbers[1]
		
	return total
			

def problem_2():
	with open('input.txt') as dataset:
		program = ''.join(dataset.read().splitlines())
		total = 0
		# preprocess lines by removing sections 
		# between a don't and a do instruction
		program = ''.join(re.split("don't\(\).*?do\(\)",program))
		

		# then remove anything after a don't that wasn't closed
		program = program[:program.find("don't")]

		multiply_instructions = re.findall('mul\(\d{1,3},\d{1,3}\)',program)
		for instruction in multiply_instructions:
			numbers = [int(x) for x in instruction[4:-1].split(',')]
			total += numbers[0] * numbers[1]
		
	return total

if __name__ == '__main__':
	print(problem_1())
	print(problem_2())




