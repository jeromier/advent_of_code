def get_map(filename='test_input.txt'):
	topo_map = []
	with open(filename) as dataset:
		for line in dataset:
			topo_map.append([int(x) for x in line.strip()])
	return topo_map

def find_all_trailheads(topo_map):
	line_index = 0
	trailheads = []

	for line in topo_map:
		for index, value in enumerate(line):
			if value == 0:
				trailheads.append((line_index,index))
		line_index += 1

	return trailheads

def traverse_map(topo_map,location, end_points):
	x, y = location
	current_height = topo_map[x][y]

	# once I reach 9, my search is done
	if current_height == 9:
		end_points.append(location)
		return

	if x - 1 >= 0 and topo_map[x-1][y] == current_height + 1:
		traverse_map(topo_map,(x-1,y), end_points)

	if x + 1 < len(topo_map) and topo_map[x+1][y] == current_height + 1:
		traverse_map(topo_map,(x+1,y), end_points)

	if y - 1 >= 0 and topo_map[x][y-1] == current_height + 1:
		traverse_map(topo_map,(x,y-1), end_points)

	if y + 1 < len(topo_map[x]) and topo_map[x][y+1] == current_height + 1:
		traverse_map(topo_map,(x,y+1), end_points)
	





def problem_1(p2=False):
	""" Do something
	"""

	total = 0
	topo_map = get_map('input.txt')
	trailheads = find_all_trailheads(topo_map)
	for trailhead in trailheads:
		peaks = []
		traverse_map(topo_map, trailhead, peaks)
		if p2 == False:
			total += len(set(peaks)) # just in case I can get to the same peak by multiple paths
		else:
			total += len(peaks)

	return total

def problem_2():
	""" Do something slightly different
	"""
	return problem_1(p2=True)

if __name__ == '__main__':
	# print(problem_1())
	print(problem_2())
	