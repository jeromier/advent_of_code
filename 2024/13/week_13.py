import re
from scipy.linalg import solve

def problem_1(p2=False):
	""" Decide how many presses of each button are required to reach the goal.
	"""
	total = 0
	with open('input.txt') as dataset:
		
		line_1 = dataset.readline().strip()
		line_2 = dataset.readline().strip()
		line_3 = dataset.readline().strip()
		line_4 = dataset.readline()

		while line_1:
			vector_1 = [int(x) for x in re.findall(r'\d+', line_1)]
			vector_2 = [int(x) for x in re.findall(r'\d+', line_2)]
			goal = [int(x) for x in re.findall(r'\d+', line_3)]

			if p2:
				goal = [10000000000000 + x for x in goal]
			

			A = [[vector_1[0],vector_2[0]], [vector_1[1], vector_2[1]]]


			movements = solve(A, goal)

			a_presses, b_presses = movements

			s1 = False
			s2 = False

			#check_solution 
			if( round(a_presses) * vector_1[0] + round(b_presses) * vector_2[0] == goal[0] and
			    round(a_presses) * vector_1[1] + round(b_presses) * vector_2[1] == goal[1]):
				s1 = True
				total += 3 * a_presses + b_presses


			line_1 = dataset.readline().strip()
			line_2 = dataset.readline().strip()
			line_3 = dataset.readline().strip()
			line_4 = dataset.readline()

		return int(total)

def problem_2():
	""" The same as p1 but the goal is much bigger
	"""
	return problem_1(p2=True)

if __name__ == '__main__':
	# print(problem_1())
	print(problem_2())
	