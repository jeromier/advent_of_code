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
		self.oriented_positions.append((x_coord,y_coord,self.orientation))

	def unique_positions(self):
		return len(set(self.positions))

class Map:

	def __init__(self, filename):
		self.map = []
		self.active_guards = []
		self.retired_guards = []
		self.guard_obstacles = []
		self.find_obstacles = False

		current_row = 0
		with open(filename) as mapfile:
			for line in mapfile:
				self.map.append(line)
				if '^' in line:
					pos = line.find('^')
					self.active_guards.append(Guard(current_row,pos,'n'))
				current_row += 1

		self.rows = len(self.map)
		self.cols = len(self.map[0])

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
				# check for guard cycles after a turn if find_obstacles is on
				if self.find_obstacles:
					self.check_for_guard_cycle()

	def check_for_guard_cycle(self):
		""" Check if we can add an obstacle that would cause a cycle.
			Consider the current directed movement
			Allow the guard to make a turn at every possible location
			Advance the guard until it would hit another obstacle.
			If at any point in that process it overlaps a previous oriented position
			that indicates a cycle
		"""

		# assuming this happens right after a turn

		for guard in self.active_guards:


			# scan the rest of the row
			x,y = guard.x, guard.y
			orientation = guard.orientation

			if orientation == 'n':
				# move along north and check cols east
				for row in range(x,-1,-1):
					for col in range(y,self.cols):

						if self.map[row][col] == '#':
							break
						if (row,col,'e') in guard.oriented_positions:
							self.guard_obstacles.append((row,y))
							break
					if self.map[row][y] == '#':
							break

			elif orientation == 'e':
				# move along east and check south
				for col in range(y,self.cols):
					for row in range(x,self.rows):
						if self.map[row][col] == '#':
							break
						if (row,col,'s') in guard.oriented_positions:
							self.guard_obstacles.append((x,col))
							break
					if self.map[x][col] == '#':
							break
			elif orientation == 's':
				# move along south and check west
				for row in range(x,self.rows):
					for col in range(y,-1,-1):
						if self.map[row][col] == '#':
							break
						if (row,col,'w') in guard.oriented_positions:
							self.guard_obstacles.append((row,y))
							break
					if self.map[row][y] == '#':
							break
			elif orientation == 'w':
				# move along west and check north
				for col in range(y,-1,-1):
					for row in range(x,-1,-1):
						if self.map[row][col] == '#':
							break
						if (row,col,'n') in guard.oriented_positions:
							self.guard_obstacles.append((x,col))
							break
					if self.map[x][col] == '#':
							break



			


def problem_1():
	current_map = Map('input.txt')

	while len(current_map.active_guards) > 0:
		current_map.step()

	print(current_map.retired_guards[0].num_turns)


	return current_map.retired_guards[0].unique_positions()

		


def problem_2():
	current_map = Map('input.txt')
	cycles = 0
	current_map.find_obstacles = True
	while len(current_map.active_guards) > 0:
		current_map.step()

	# print(current_map.guard_obstacles)
	#print(current_map.retired_guards[0].positions)
	# print("positions:",current_map.retired_guards[0].unique_positions())
	return len(current_map.guard_obstacles)


if __name__ == '__main__':
	# print(problem_1())
	print(problem_2())