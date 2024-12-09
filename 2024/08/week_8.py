from operator import sub
from operator import add

def problem_1(find_all=False):
	""" Do something
	"""
	rows = 0
	cols = 0
	antennas = {}
	with open('input.txt') as dataset:

		# get the location of every antenna and put it in a dictionary
		for row, line in enumerate(dataset):
			rows = row + 1
			for col, value in enumerate(line.strip()):
				cols = col + 1
				if value != '.':
					if value in antennas:
						antennas[value].append((row,col))
					else:
						antennas[value] = [(row,col)]

		antinodes = set()
		
		# pair every antenna with every other like antenna
		# find the slope between them
		# find the new next point in those lines
		for locations in antennas.values():
			for i, a1 in enumerate(locations):
				for a2 in locations[i+1:]:
					slope = tuple(map(sub, a1,a2))
					antinode1 = tuple(map(add,a1,slope))
					antinode2 = tuple(map(sub,a2,slope))

					if not find_all:
						
						# code for problem 1
						if 0 <= antinode1[0] < rows and 0 <= antinode1[1] < cols:
							antinodes.add(antinode1)

						if 0 <= antinode2[0] < rows and 0 <= antinode2[1] < cols:
							antinodes.add(antinode2)
					else:
						# code for problem 2
						antinodes.add(a1)
						antinodes.add(a2)

						while 0 <= antinode1[0] < rows and 0 <= antinode1[1] < cols:
							antinodes.add(antinode1)
							antinode1 = tuple(map(add,antinode1,slope))

						while 0 <= antinode2[0] < rows and 0 <= antinode2[1] < cols:
							antinodes.add(antinode2)
							antinode2 = tuple(map(sub,antinode2,slope))



		return len(antinodes)

def problem_2():
	""" Do something slightly different
	"""
	return problem_1(find_all=True)

if __name__ == '__main__':
	# print(problem_1())
	print(problem_2())
	