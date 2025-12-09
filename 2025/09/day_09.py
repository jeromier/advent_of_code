import shapely

def get_red_tiles(filename='example.txt'):
	with open(filename) as tile_list:
		tiles = [tuple(map(int,t.split(','))) for t in tile_list.read().splitlines()]
	return tiles

def get_max_area(tiles):
	area = 0
	for i in range(len(tiles)):
		for j in range(i+1,len(tiles)):
			new_area = (abs(tiles[i][0]-tiles[j][0])+1) * (abs(tiles[i][1]-tiles[j][1])+1)
			area = new_area if new_area > area else area
	return area

def get_all_rectangles(tiles):
	rectangles = []
	for i in range(len(tiles)):
		for j in range(i+1,len(tiles)):
			area = (abs(tiles[i][0]-tiles[j][0])+1) * (abs(tiles[i][1]-tiles[j][1])+1)
			rectangles.append([area,[tiles[i],tiles[j]]])
	return sorted(rectangles,reverse=True)

def get_full_rectangle(rectangle):
	"""Use the two corner points of a rectangle
	to find the other points."""
	points = []
	point_a = rectangle[1][0]
	point_b = rectangle[1][1]
	points.append(point_a)
	points.append((point_a[0],point_b[1]))
	points.append(point_b)
	points.append((point_b[0],point_a[1]))
	points.append(point_a) # initial point repeated for shapely
	return points


def p1(filename='example.txt'):
	tiles = get_red_tiles(filename)
	area = get_max_area(tiles)
	return area

def p2(filename='example.txt'):
	tiles = get_red_tiles(filename)
	rectangles = get_all_rectangles(tiles)
	red_and_green = shapely.Polygon(tiles + [tiles[0]])

	for rectangle in rectangles:
		rect = get_full_rectangle(rectangle)
		if red_and_green.contains(shapely.Polygon(rect)):
			return rectangle[0]

	return 0

# print(p1('input.txt'))
print(p2('input.txt'))
