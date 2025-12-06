import math

def get_answer(problem):
	numbers = [int(i) for i in problem[:-1]]
	operator = problem[-1]
	if operator == '*':
		answer = math.prod(numbers)
	elif operator == '+':
		answer = sum(numbers)
	return answer


def solve_math_worksheet_p1(filename='example.txt'):
	with open(filename) as math_worksheet:
		problems = [line.split() for line in math_worksheet.read().splitlines()]
		problems = list(zip(*problems))

	total = 0
	for problem in problems:
		total += get_answer(problem)
	return total

def solve_math_worksheet_p2(filename='example.txt'):
	with open(filename) as math_worksheet:
		problems = math_worksheet.read().splitlines()

	total = 0
	# start at the end
	index = len(problems[0]) - 1
	# the operators are in the last row
	operators = len(problems) - 1
	
	# build up each problem one at a time
	
	while index >= 0:
		problem = []
		while True:
			number = ''
			for row in problems[:-1]:
				number += row[index]
			problem.append(number)
			if problems[operators][index] == ' ':
				index -= 1
			else:
				problem.append(problems[operators][index])
				index -= 2 # skip the blank column
				break
		total += get_answer(problem)

	return total

		




print(solve_math_worksheet_p1('input.txt'))
print(solve_math_worksheet_p2('input.txt'))