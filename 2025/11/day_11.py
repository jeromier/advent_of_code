from collections import defaultdict

class ServerGraph(object):
	"""Keep track of the Elves' servers"""
	def __init__(self):
		self.servers = defaultdict(list)
		self.exits_from = defaultdict(int)

	def load_from_file(self,filename):
		with open(filename) as server_file:
			for line in server_file:
				node, children = line.split(':')
				children = children.strip().split()
				self.servers[node] = children

	def count_exits(self,start='you',target='out', visited=None):
		""" Standard DFS for exits."""

		if visited is None:
			visited = set()

		# don't go down this path if we've already visited this node
		# during the current path traversal
		if start in visited:
			return 0

		# add self to set of visited nodes
		visited.add(start)

		# default situation that ends the search
		if start == target:
			return 1

		exits = 0
		for child in self.servers[start]:
			if child in self.exits_from:
				exits += self.exits_from[child]
			else:
				exits += self.count_exits(child, target, visited.copy())

		# found all of the exits from this point, so I don't need to count this path again
		self.exits_from[start] = exits

		return exits

def p1(filename='example.txt'):
	sg = ServerGraph()
	sg.load_from_file(filename)
	exits = sg.count_exits()
	return exits

def p2(filename='example2.txt'):
	sg = ServerGraph()
	sg.load_from_file(filename)
	exits = sg.count_exits(start='svr',target='fft')
	svr_to_fft = exits

	sg = ServerGraph()
	sg.load_from_file(filename)
	exits = sg.count_exits(start='fft',target='dac')
	fft_to_dac = exits

	sg = ServerGraph()
	sg.load_from_file(filename)
	exits = sg.count_exits(start='dac',target='out')
	dac_to_out = exits

	return svr_to_fft * fft_to_dac * dac_to_out

print(p1('input.txt'))
print(p2('input.txt'))

		