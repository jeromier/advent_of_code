def blink_without_dups(stones):
	""" Transform the stones according to the rules.
		1) If value = 0, replace with 1
		2) If even number of digits, split
		3) Else multiply by 2024

		stones: a list of integers

		this version works on a dictionary instead of a list
	"""
	

	new_stones = {}
	for stone in stones:
		if stone == 0:
			if 1 not in new_stones:
				new_stones[1] = stones[0] # add a 1 for each zero
			else:
				new_stones[1] += stones[0]

		elif len(str(stone)) % 2 == 0:
			stone_str = str(stone)
			middle = len(stone_str) // 2
			value1 = int(stone_str[:middle])
			value2 = int(stone_str[middle:])

			if value1 not in new_stones:
				new_stones[value1] = stones[stone]
			else:
				new_stones[value1] += stones[stone]

			if value2 not in new_stones:
				new_stones[value2] = stones[stone]
			else:
				new_stones[value2] += stones[stone]
		
		else:
			if stone * 2024 not in new_stones:
				new_stones[stone * 2024] = stones[stone]
			else:
				new_stones[stone * 2024] += stones[stone]

	return new_stones



def blink(stones):
	""" Transform the stones according to the rules.
		1) If value = 0, replace with 1
		2) If even number of digits, split
		3) Else multiply by 2024

		stones: a list of integers

		No longer used, but kept for posterity
	"""
	new_stones = []
	for stone in stones:
		if stone == 0:
			new_stones.append(1)
		elif len(str(stone)) % 2 == 0:
			stone_str = str(stone)
			middle = len(stone_str) // 2

			new_stones.append(int(stone_str[:middle]))
			new_stones.append(int(stone_str[middle:]))
		else:
			new_stones.append(stone * 2024)

	return new_stones

def problem_1():
	""" read the file and follow the blinking rules 25 times
	"""
	return blink_n(25)

def problem_2():
	""" read the file and follow the blinking rules 75 times
	"""
	return blink_n(75)

def blink_n(num_blinks):
	""" read the file and follow the blinking rules without duplicates
	"""
	with open('input.txt') as dataset:
		stones = [int(x) for x in dataset.read().strip().split()]
		stones_dict = {}
		for stone in set(stones):
			stones_dict[stone] = stones.count(stone)

		for i in range(num_blinks):
			stones_dict = blink_without_dups(stones_dict)

		total = 0
		for stone in stones_dict:
			total += stones_dict[stone]

	return total

if __name__ == '__main__':
	print(problem_1())
	print(problem_2())
	