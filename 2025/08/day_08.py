import math
from operator import sub

def read_points(filename='example.txt'):
	points = []
	with open(filename) as point_file:
		for line in point_file:
			points.append(tuple(map(int,line.strip().split(','))))
	return points
	
def distance(a,b):
	return math.sqrt(sum([x**2 for x in map(sub,b,a)]))

def get_distances(points):
	distances = []
	for i in range(len(points)):
		for j in range(i+1,len(points)):
			distances.append((distance(points[i],points[j]),i,j))
	return sorted(distances)

def add_to_circuit(circuits,a,b):
	added = False
	# if either node is in an existing circuit, add it to that one
	for circuit in circuits:
		if a in circuit or b in circuit:
			circuit.add(a)
			circuit.add(b)
			added = True
			break # only need to add it to one. I will merge all overlapping sets later
	# otherwise, create a new circuit and add it
	if not added:
		circuits.append(set((a,b)))

def merge_circuits(circuits):
	merge_happened = False
	
	for i in range(len(circuits)):
		for j in range(i+1,len(circuits)):
			if not circuits[i].isdisjoint(circuits[j]):
				circuits[i] |= circuits[j]
				circuits.pop(j)
				merge_happened = True
				break
				
	return merge_happened
				

def p1(filename='example.txt',connections=10):
	circuits = []
	points = read_points(filename)
	distances = get_distances(points)
	for connection in distances[:connections]:
		add_to_circuit(circuits,connection[1],connection[2])
	merge_happened = merge_circuits(circuits)
	while merge_happened:
		merge_happened = merge_circuits(circuits)
	# multiply length of three longest circuits
	total = math.prod(sorted([len(circuit) for circuit in circuits],reverse=True)[:3])
	return total

def p2(filename='example.txt'):
	circuits = []
	points = read_points(filename)
	distances = get_distances(points)
	distance_index = 0
	connected_points = set()
	
	# add connections until every point is connected
	while len(connected_points) < len(points):
		connection = distances[distance_index]
		add_to_circuit(circuits,connection[1],connection[2])
		distance_index += 1
		
		connected_points.add(connection[1])
		connected_points.add(connection[2])
	
	# merge circuits	
	merge_happened = merge_circuits(circuits)
	while merge_happened:
		merge_happened = merge_circuits(circuits)
	
	# add a new connection and merge until there is one circuit
	while len(circuits) > 1:
		# add connection
		connection = distances[distance_index]
		add_to_circuit(circuits,connection[1],connection[2])
		distance_index += 1
			
		# merge circuits	
		merge_happened = merge_circuits(circuits)
		while merge_happened:
			merge_happened = merge_circuits(circuits)
	
	return points[connection[1]][0] * points[connection[2]][0]
	

#print(p1())
#print(p1('input.txt',connections=1000))
print(p2('input.txt'))

