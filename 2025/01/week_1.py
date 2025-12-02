# Advent of Code 2025, Week 1

def get_code(filename='example.txt',start=50):
	
	# Get the combination as positive and negative numbers
	combination = []
	with open(filename) as combo_file:
		for line in combo_file.readlines():
			data = line.strip()
			if data[0] == 'L':
				combination.append(-1 * int(data[1:]))
			else:
				combination.append(int(data[1:]))
	
	# calculate how many zeros	
	running_total = start
	zeroes = 0
	all_crossed_zeroes = 0
	
	# It will cross zero if it goes from positive to negative
	# and once for every 100 you turn it (unless it started on zero)
	
	for rotation in combination:
		crossed_zeroes = 0
		
		# cross zero for every 100 we would rotate
		crossed_zeroes += abs(rotation) // 100
		
		# reduce rotation by crossed zeroes
		if rotation >= 0:
			rotation = rotation % 100
		else:
			rotation = rotation % -100
	
		# add the remaining rotation
		old_total = running_total
		running_total += rotation 
		
		# take away one if we started and ended on zero
		if crossed_zeroes > 0 and old_total == 0 and running_total == 0:
			crossed_zeroes -= 1
		
		# check if we crossed zero with the remaining rotation
		if (running_total < 0 and old_total > 0) or running_total > 100:
			crossed_zeroes += 1
		
		# properly set the position on the dial using modulus	
		running_total = running_total % 100
		
		# Add one to the total if we ended on zero
		if running_total == 0:
			zeroes += 1
		
		all_crossed_zeroes += crossed_zeroes
	
	# Return values for simple program and more advanced program
	return zeroes, zeroes + all_crossed_zeroes
	
print(get_code('input.txt'))
		
		
		
