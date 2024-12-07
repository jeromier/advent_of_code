def check_possible_operators(solution,numbers,concat=False):
	possible_solutions = []

	# reverse the list once so that I can pop items from the back
	# which should be a little faster
	numbers.reverse()

	# seed the solutions list
	possible_solutions.append(numbers.pop())

	while len(numbers) > 0:
		next_number = numbers.pop()
		next_step = []

		for sol in possible_solutions:
			n = sol * next_number
			if n <= solution:
				next_step.append(n)

			n = sol + next_number
			if n <= solution:
				next_step.append(n)

			if concat:
				n = int(str(sol) + str(next_number))
				if n <= solution:
					next_step.append(n)

		# possibly expensive operation
		possible_solutions = next_step[:]

	if solution in possible_solutions:
		return True
	else:
		return False

def problem_1(concat=False):
	""" Take a list of numbers and see if we can find a solution using + and *
	"""
	total = 0
	with open('input.txt') as dataset:
		for line in dataset:
			equation = line.split(':')
			solution = int(equation[0])
			numbers = [int(x) for x in equation[1].split()]
			if check_possible_operators(solution,numbers,concat):
				total += solution

		return total

def problem_2():
	""" Same as problem 1, but add a concat operator
	"""
	return problem_1(concat=True)

if __name__ == '__main__':
	# print(problem_1())
	print(problem_2())
	