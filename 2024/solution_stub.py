def parse_file(test=False):
	filename = 'input.txt'
	if test:
		filename = ('test_input.txt')

	with open(filename) as dataset:
		# do stuff here
		return

def problem_1(test=False):
	data = parse_file(test)
	return 0

def problem_2(test=False):
	data = parse_file(test)
	return 0

def run_tests():
	problem_1_solution = 0
	problem_2_solution = 0

	if problem_1(test=True) == problem_1_solution:
		print("Problem 1 passes the test")
	else:
		print("Problem 1 fails the test")

	if problem_2(test=True) == problem_2_solution:
		print("Problem 2 passes the test")
	else:
		print("Problem 2 fails the test")

if __name__ == '__main__':
	run_tests()

	print("The answer to problem 1 is," problem_1())
	print("The answer to problem 2 is," problem_2())




