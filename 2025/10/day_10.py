import numpy
from scipy.optimize import milp
from scipy.optimize import LinearConstraint

class Machine:

	def __init__(self, goal, wiring, joltage):
		self.goal = goal # string indicating target lights
		self.wiring = wiring # list of tuples with button wiring
		self.joltage_goal = [int(i) for i in joltage.strip('{}').split(',')] # will be used in the future

	def light_presses(self):
		"""Find minimum presses to reach the goal"""
		start = '.'*len(self.goal)
		all_states = [start]
		depth = 0

		while self.goal not in all_states:
			next_states = []
			for state in all_states:
				for button in self.wiring:
					temp_state = list(state)
					for i in button:
						if temp_state[i] == '.':
							temp_state[i] = '#'
						else:
							temp_state[i] = '.'
					temp_state = ''.join(temp_state)
					if temp_state not in next_states:
						next_states.append(''.join(temp_state))
			depth += 1
			all_states = next_states

		return depth

	def joltage_presses(self):
		"""Find minimum presses to reach the goal"""

		# Solve equation of type ax = b
		# setup a matrix
		buttons = []
		for button in self.wiring:
			row = [0] * len(self.joltage_goal)
			for wire in button:
				row[wire] =1
			buttons.append(row)


		a= numpy.array(buttons)
		b = numpy.array(self.joltage_goal)
		c=numpy.ones(len(buttons)) # just a simple identity vector--the problem is all in the contraints

		integrality = numpy.ones_like(c) # solutions must be integers
		constraints = LinearConstraint(a.T,lb=b,ub=b) # Using the buttons array and requiring the results to be the output joltage

		# using python's mixed integer linear programming solver
		res = milp(c=c,constraints=constraints,integrality=integrality)
		
		return sum(res.x)


def get_schematics(filename='example.txt'):
	machines = []
	with open(filename) as machine_file:
		machine_data = machine_file.read().splitlines()

	for m in machine_data:
		m = m.split()
		wiring = []
		for button in m[1:-1]:
			wiring.append(tuple([int(i) for i in button.strip('()').split(',')]))
		machines.append(Machine(m[0].strip('[]'), wiring , m[-1]))

	return machines

def p1(filename='example.txt'):
	machines = get_schematics(filename)
	total_presses = 0
	for machine in machines:
		total_presses += machine.light_presses()
	return total_presses

def p2(filename='example.txt'):
	machines = get_schematics(filename)
	total_presses = 0
	machine_number = 1
	for machine in machines:
		total_presses += machine.joltage_presses()
		machine_number += 1
	return int(total_presses)


# print(p1('input.txt'))
print(p2('input.txt'))


