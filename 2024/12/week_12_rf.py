def find_region_dimensions(location, garden, visited, region_id, regions):
	x, y = location
	visited[x][y] = True

	# Add this spot to the area of the current region
	if region_id in regions:
		regions[region_id][0] += 1
	else:
		regions[region_id] = [1,0]

	# Check N/E/S/W neighbors
	# If the neighbor is not in the region, add one to the perimeter
	# If it is in the region, visit it if it has not already been visited

	# North
	if x - 1 < 0 or garden[x-1][y] != garden[x][y]:
		regions[region_id][1] += 1
	else:
		if not visited[x-1][y]:
			find_region_dimensions((x-1, y), garden, visited, region_id, regions)

	# East
	if y + 1 >= len(garden[x]) or garden[x][y+1] != garden[x][y]:
		regions[region_id][1] += 1
	else:
		if not visited[x][y+1]:
			find_region_dimensions((x, y+1), garden, visited, region_id, regions)

	# South
	if x + 1 >= len(garden) or garden[x+1][y] != garden[x][y]:
		regions[region_id][1] += 1
	else:
		if not visited[x+1][y]:
			find_region_dimensions((x+1, y), garden, visited, region_id, regions)


	# West
	if y - 1 < 0 or garden[x][y-1] != garden[x][y]:
		regions[region_id][1] += 1
	else:
		if not visited[x][y-1]:
			find_region_dimensions((x, y-1), garden, visited, region_id, regions)


def problem_1():
	""" Find the perimiter and area of each garden in the map
	"""
	
	total = 0
	with open('test_input.txt') as dataset:
		
		# read the map
		garden = dataset.read().splitlines()

		# create a 2d list of identical size to the map
		# to keep track of which plots we've visited
		visited = [ [False] * len(garden[0]) for x in range(len(garden))]

		# Create a region_id
		region_id = 0

		# Create a dictionary to store information about each region
		# Each region will be a list of 2 elements representing area and perimeter
		regions = {0 : [0,0]}

		
		for x, row in enumerate(garden):
			for y, plot in enumerate(row):
				if not visited[x][y]:
					find_region_dimensions((x,y), garden, visited, region_id, regions)
					region_id += 1

		for area, perimeter in regions.values():
			total += area * perimeter

		return total

def problem_2():
	""" Find the perimiter and area of each garden in the map
	"""
	
	total = 0
	with open('test_input.txt') as dataset:
		
		# read the map
		garden = dataset.read().splitlines()

		# create a 2d list of identical size to the map
		# to keep track of which plots we've visited
		visited = [ [False] * len(garden[0]) for x in range(len(garden))]

		# set up sides
		sides = [ [(False, False, False, False)] * len(garden[0]) for x in range(len(garden))]


		# Create a region_id
		region_id = 0

		# Create a dictionary to store information about each region
		# Each region will be a list of 2 elements representing area and perimeter
		regions = {0 : [0,0]}

		
		for x, row in enumerate(garden):
			for y, plot in enumerate(row):
				if not visited[x][y]:
					find_region_dimensions_sides((x,y), garden, visited, region_id, regions, sides)
					region_id += 1


		print(regions)

		for area, sides in regions.values():
			total += area * sides

		return total

if __name__ == '__main__':
	# print(problem_1())
	print(problem_2())

	