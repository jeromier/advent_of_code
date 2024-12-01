import string

# Part 1
total = 0
with open('input.txt') as dataset:
	for line in dataset:
		text=line.strip().strip(string.ascii_letters)
		first_digit = text[0]
		last_digit = text[-1]
		total += int(first_digit + last_digit)

print(total)

# Part 2
total = 0
digits = {
		'one':'1',
		'two':'2',
		'three':'3',
		'four':'4',
		'five':'5',
		'six':'6',
		'seven':'7',
		'eight':'8',
		'nine':'9',
		'0':'0',
		'1':'1',
		'2':'2',
		'3':'3',
		'4':'4',
		'5':'5',
		'6':'6',
		'7':'7',
		'8':'8',
		'9':'9'
		}
with open('input.txt') as dataset:
	for line in dataset:
		# find left most digit
		
		left_most_digit_position = -1
		left_most_digit = ''

		for digit in digits.keys():
			pos = line.find(digit)
			if pos >= 0 and (left_most_digit_position == -1 or pos < left_most_digit_position):
				left_most_digit_position = pos
				left_most_digit = digit

		# find right most digit

		right_most_digit_position = -1
		right_most_digit = ''

		for digit in digits.keys():
			pos = line.rfind(digit)
			if pos >= 0 and pos > right_most_digit_position:
				right_most_digit_position = pos
				right_most_digit = digit

	
		first_digit = digits[left_most_digit]
		last_digit = digits[right_most_digit]

		total += int(first_digit + last_digit)

print(total)