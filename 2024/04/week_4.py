def problem_1():
	""" Find all occurrences of XMAS in a grid of strings
	"""
	total_xmas = 0
	with open('input.txt') as dataset:
		word_search = dataset.read().splitlines()

		rows = len(word_search)
		cols = len(word_search[0])

		# find horizontal XMAS
		for line in word_search:
			total_xmas += line.count('XMAS')
			total_xmas += line.count('SAMX')

		# find vertical XMAS
		for row in range(rows-3):
			for col in range(cols):
				if (word_search[row][col] == 'X' 
					and word_search[row+1][col] == 'M'
					and word_search[row+2][col] == 'A'
					and word_search[row+3][col] == 'S'):
					total_xmas += 1
				if (word_search[row][col] == 'S' 
					and word_search[row+1][col] == 'A'
					and word_search[row+2][col] == 'M'
					and word_search[row+3][col] == 'X'):
					total_xmas += 1

		# find forward diagonal XMAS
		for row in range(rows-3):
			for col in range(cols-3):
				if (word_search[row][col] == 'X' 
					and word_search[row+1][col+1] == 'M'
					and word_search[row+2][col+2] == 'A'
					and word_search[row+3][col+3] == 'S'):
					total_xmas += 1
				if (word_search[row][col] == 'S' 
					and word_search[row+1][col+1] == 'A'
					and word_search[row+2][col+2] == 'M'
					and word_search[row+3][col+3] == 'X'):
					total_xmas += 1

		# find backward diagonal XMAS
		for row in range(rows-3):
			for col in range(3,cols):
				if (word_search[row][col] == 'X' 
					and word_search[row+1][col-1] == 'M'
					and word_search[row+2][col-2] == 'A'
					and word_search[row+3][col-3] == 'S'):
					total_xmas += 1
				if (word_search[row][col] == 'S' 
					and word_search[row+1][col-1] == 'A'
					and word_search[row+2][col-2] == 'M'
					and word_search[row+3][col-3] == 'X'):
					total_xmas += 1

		return total_xmas

def problem_2():
	""" Find all places where MAS cross diagonally
	"""
	total_xmas = 0
	with open('input.txt') as dataset:
		word_search = dataset.read().splitlines()

		rows = len(word_search)
		cols = len(word_search[0])

		forward_as = []
		backward_as = []

		# find forward diagonal MAS
		for row in range(rows-2):
			for col in range(cols-2):
				if (word_search[row][col] == 'M'
					and word_search[row+1][col+1] == 'A'
					and word_search[row+2][col+2] == 'S'):
					forward_as.append((row+1,col+1))
				if (word_search[row][col] == 'S' 
					and word_search[row+1][col+1] == 'A'
					and word_search[row+2][col+2] == 'M'):
					forward_as.append((row+1,col+1))

		# find backward diagonal MAS
		for row in range(rows-2):
			for col in range(2,cols):
				if (word_search[row][col] == 'M'
					and word_search[row+1][col-1] == 'A'
					and word_search[row+2][col-2] == 'S'):
					backward_as.append((row+1,col-1))
				if (word_search[row][col] == 'S' 
					and word_search[row+1][col-1] == 'A'
					and word_search[row+2][col-2] == 'M'):
					backward_as.append((row+1,col-1))

		for a in forward_as:
			if a in backward_as:
				total_xmas += 1
		return total_xmas

if __name__ == '__main__':
	#print(problem_1())
	print(problem_2())
	