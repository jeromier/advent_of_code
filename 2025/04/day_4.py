def get_floorplan(filename='example.txt'):

	with open(filename) as map_file:
		floorplan = [list(line.strip()) for line in map_file.readlines()]

	return floorplan

def get_accessible_rolls(floorplan):

	rows = len(floorplan)
	cols = len(floorplan[0])

	accessible_rolls = 0

	for r in range(rows):
		for c in range(cols):
			if floorplan[r][c] == '@' and check_neighbors(floorplan,r,c,rows,cols) < 4:
				floorplan[r][c] = '.' # remove the roll
				accessible_rolls += 1
	return accessible_rolls


def check_neighbors(floorplan, r, c, rows, cols):
	count = 0
	if r > 0 and c > 0 and floorplan[r-1][c-1] == '@':
		count += 1
	if r > 0 and floorplan[r-1][c] == '@':
		count += 1
	if r > 0 and c < cols-1 and floorplan[r-1][c+1] == '@':
		count += 1
	
	if c > 0 and floorplan[r][c-1] == '@':
		count += 1
	if c < cols-1 and floorplan[r][c+1] == '@':
		count += 1

	if r < rows-1 and c > 0 and floorplan[r+1][c-1] == '@':
		count += 1
	if r < rows-1 and floorplan[r+1][c] == '@':
		count += 1
	if r < rows-1 and c < cols-1 and floorplan[r+1][c+1] == '@':
		count += 1

	return count

def p1(filename='example.txt'):
	return get_accessible_rolls(get_floorplan(filename))

def p2(filename='example.txt'):
	floorplan = get_floorplan(filename)

	total_rolls = 0
	rolls = get_accessible_rolls(floorplan)
	while rolls > 0:
		total_rolls += rolls
		rolls = get_accessible_rolls(floorplan)
	return total_rolls

# print(p1('input.txt'))
print(p2('input.txt'))