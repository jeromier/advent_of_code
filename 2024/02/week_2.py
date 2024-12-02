def is_safe(report):
	""" A report is safe if it is either solely increasing or
		solely decreasing AND the distance between two adjacent
		numbers is never greater than 3.

		report -- a list of integers
	"""
	if report[1] - report[0] > 0:
		increasing = True
	else:
		increasing = False

	for i in range(1,len(report)):
		step = report[i] - report[i-1]
		if increasing:
			if not (step > 0 and abs(step) <=3):
				return False
		else:
			if not (step < 0 and abs(step) <=3):
				return False
	return True

def is_safe_with_dampener(report):
	""" Checks if an unsafe report (see is_safe) can be
		made safe by the removal of one value from the list.

		report -- a list of integers

	"""
	positive_polarity = [] # index of increasing numbers
	negative_polarity = [] # index of decreasing numbers
	magnitude_errors = [] # change of 0 or > 3

	for i in range(1,len(report)):
		step = report[i] - report[i-1]
		if step > 0:
			positive_polarity.append(i)
		else:
			negative_polarity.append(i)
		if abs(step) > 3 or step == 0:
			magnitude_errors.append(i)

	# Return true and end if there are no errors
	if ((len(positive_polarity) == 0 or len(negative_polarity) == 0) and 
		len(magnitude_errors) == 0):
		return True

	# Try to fix errors

	# try to fix a polarity error

	if len(positive_polarity) > 0 and len(negative_polarity) > 0:
		# If there is more than one polarity error, it cannot be fixed
		if len(positive_polarity) > 1 and len(negative_polarity) > 1:
			return False

		
		# The problem index is the one spot where the polarity is different
		if len(positive_polarity) == 1:
			problem_index = positive_polarity[0]
		else:
			problem_index = negative_polarity[0]

		# It could be fixed by removing the element where the error showed up
		# or the one right before it
		if (is_safe(report[:problem_index-1] + report[problem_index:]) or
			is_safe(report[:problem_index] + report[problem_index+1:])):
			return True

		# couldn't fix the polarity error
		return False

	# try to fix a magnitude error

	# if there are more than two magnitude errors, it cannot be fixed
	# (It's possible for a single value to cause two errors)
	if len(magnitude_errors) > 2:
		return False

	# I only have to check the first index
	problem_index = magnitude_errors[0]

	# A magnitude error can possibly be fixed by removing the element
	# where the problem was identified OR the one before it
	if (is_safe(report[:problem_index-1] + report[problem_index:]) or
		is_safe(report[:problem_index] + report[problem_index+1:])):
		return True

	# We weren't able to fix the error(s) so return false
	return False

def problem_1():
	safe_lines = 0
	with open('input.txt') as dataset:
		for line in dataset:
			report = [int(x) for x in line.split()]
			if is_safe(report):
				safe_lines += 1
	return safe_lines
			

def problem_2():
	safe_lines = 0
	with open('input.txt') as dataset:
		for line in dataset:
			report = [int(x) for x in line.split()]
			if is_safe_with_dampener(report):
				safe_lines += 1
	return safe_lines

if __name__ == '__main__':
	print(problem_1())
	print(problem_2())




