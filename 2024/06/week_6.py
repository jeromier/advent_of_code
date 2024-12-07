import copy

class Guard:

	directions = 'nesw'

	def __init__(self,x_coord,y_coord,orientation):
		self.x = x_coord
		self.y = y_coord
		self.orientation = orientation
		
		self.positions = [(x_coord,y_coord)]
		self.oriented_positions = [(x_coord,y_coord,orientation)]

	def turn_right(self):
		# set the new orientation
		direction_index = self.directions.find(self.orientation)
		self.orientation = self.directions[(direction_index + 1) % 4]
		self.oriented_positions.append((self.x,self.y,self.orientation))

	def move(self):
		""" Return next location in given direction
			Does NOT actually update the position
			Assumes 0,0 is upper left corner of the map
		"""
		direction = self.orientation
		if direction == 'n':
			return (self.x-1,self.y)
		elif direction == 'e':
			return (self.x,self.y+1)
		elif direction == 's':
			return (self.x+1, self.y)
		elif direction == 'w':
			return (self.x, self.y-1)
		else:
			raise ValueError('Invalid direction')


	def update_position(self,x_coord, y_coord):
		self.x = x_coord
		self.y = y_coord
		self.positions.append((x_coord,y_coord))

		assert (x_coord,y_coord,self.orientation) not in self.oriented_positions
		self.oriented_positions.append((x_coord,y_coord,self.orientation))

	def unique_positions(self):
		return len(set(self.positions))

class Map:

	def __init__(self, filename):
		self.map = []
		self.active_guards = []
		self.initial_guards = []
		self.retired_guards = []
		self.guard_obstacles = []

		current_row = 0
		with open(filename) as mapfile:
			for line in mapfile:
				self.map.append(list(line))
				if '^' in line:
					pos = line.find('^')
					self.active_guards.append(Guard(current_row,pos,'n'))
					self.initial_guards.append(Guard(current_row,pos,'n'))
				current_row += 1


		self.rows = len(self.map)
		self.cols = len(self.map[0])

	def add_obstacle(self,x,y):
		self.map[x][y] = '#'

	def remove_obstacle(self,x,y):
		self.map[x][y] = '.'

	def reset_guards(self):
		self.active_guards = []
		for guard in self.initial_guards:
			self.active_guards.append(Guard(guard.x,guard.y,'n'))

	def step(self):
		for guard in self.active_guards:
			x,y = guard.move()

			# If the guard would move off the map, move them from active to retired
			if x < 0 or y < 0 or x >= self.rows or y >= self.cols:
				self.retired_guards.append(guard)
				self.active_guards.remove(guard)
				continue
			
			if self.map[x][y] != '#':
				guard.update_position(x,y)
			else:
				guard.turn_right()
			


def problem_1():
	current_map = Map('input.txt')

	while len(current_map.active_guards) > 0:
		current_map.step()

	return current_map.retired_guards[0].unique_positions()

		


def problem_2():
	current_map = Map('input.txt')
	cycles = 0
	current_map.find_obstacles = True
	while len(current_map.active_guards) > 0:
		current_map.step()

	# get the entire path except for the starting point
	path = set(current_map.retired_guards[0].positions[1:])

	loops = 0

	iterations = 0
	for location in path:
		iterations += 1
		print('testing',iterations,'of',len(path))
		current_map.reset_guards()
		try:
			current_map.add_obstacle(location[0],location[1])
			while len(current_map.active_guards) > 0:
				current_map.step()
		except AssertionError:
			loops+=1
		finally:
			current_map.remove_obstacle(location[0],location[1])

	return loops


if __name__ == '__main__':
	# print(problem_1())
	print(problem_2())