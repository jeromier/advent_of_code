def read_manifold(filename='example.txt'):
	with open(filename) as manifold_file:
		manifold = manifold_file.read().splitlines()
	return manifold

def count_splits(manifold):
	splits = 0
	positions = set()
	positions.add(manifold[0].find('S'))
	current_row = 1
	while current_row < len(manifold):
		next_positions = set()
		for pos in positions:
			if manifold[current_row][pos] == '^':
				splits += 1
				# should probably check boundaries
				# but I looked at the input and don't think it's necessary
				next_positions.add(pos-1)
				next_positions.add(pos+1)
			else:
				next_positions.add(pos)
		positions = next_positions
		current_row += 1
	return splits

def count_quantum_splits(manifold):
	positions = {}
	start_point = manifold[0].find('S')
	positions[start_point] = 1
	current_row = 1

	while current_row < len(manifold):
		next_positions = {}
		for pos, count in positions.items():
			if manifold[current_row][pos] == '^':
				if pos-1 in next_positions:
					next_positions[pos-1] += count
				else:
					next_positions[pos-1] = count

				if pos+1 in next_positions:
					next_positions[pos+1] += count
				else:
					next_positions[pos+1] = count
			else:
				if pos in next_positions:
					next_positions[pos] += count
				else:
					next_positions[pos] = count
		positions = next_positions
		current_row += 1

	
	return sum(positions.values())


def p1(filename='example.txt'):
	return count_splits(read_manifold(filename))

def p2(filename='example.txt'):
	return count_quantum_splits(read_manifold(filename))

print(p1('input.txt'))
print(p2('input.txt'))

