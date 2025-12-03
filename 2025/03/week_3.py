def joltage(bank):
	# find the largest digit, but leave at least one at the end
	first_digit, first_index = largest_digit(bank[:-1])
	# get the largest digit from the remainder
	second_digit, second_index = largest_digit(bank[first_index+1:])
	return(int(first_digit+second_digit))

def joltage12(bank):
	digits = ''
	# get the largest digit, leaving enough at the end to search for remaining digits
	# need to make a 12 digit number
	for i in range(-11,1):
		if i != 0:
			digit, index = largest_digit(bank[:i])
		else:
			digit, index = largest_digit(bank)
		digits += digit
		bank = bank[index+1:]

	return int(digits)

def largest_digit(num_string):
	largest = '0'
	index = 0
	i = 0

	for digit in num_string:
		if digit > largest:
			largest = digit
			index = i
		i += 1
		if digit == '9':
			break

	return largest, index

def total_joltage(filename='example.txt'):
	total_j = 0

	with open(filename) as battery_banks:
		for line in battery_banks:
			total_j += joltage(line.strip())

	return total_j

def joltage_override(filename='example.txt'):
	total_j = 0

	with open(filename) as battery_banks:
		for line in battery_banks:
			total_j += joltage12(line.strip())

	return total_j


print(total_joltage('input.txt'))
print(joltage_override('input.txt'))

