import numpy
import scipy.signal

def convert_to_digits(roll):
	if roll == '@':
		return 1
	else:
		return 0

def get_floorplan(filename='example.txt'):

	with open(filename) as map_file:
		floorplan = numpy.array([list(map(convert_to_digits,line.strip())) for line in map_file.readlines()])

	return floorplan

def get_accessible_rolls(floorplan):
	counts = scipy.signal.convolve2d(floorplan, numpy.ones((3,3)), mode='same')
	only_rolls = counts*floorplan
	return (only_rolls < 5).sum() - (only_rolls == 0).sum()

def get_accessible_rolls_p2(floorplan):
	counts = scipy.signal.convolve2d(floorplan, numpy.ones((3,3)), mode='same')
	only_rolls = counts*floorplan
	rolls = (only_rolls < 5).sum() - (only_rolls == 0).sum()
	total_rolls = rolls
	while rolls > 0:
		floorplan[counts < 5] = 0
		counts = scipy.signal.convolve2d(floorplan, numpy.ones((3,3)), mode='same')
		only_rolls = counts*floorplan
		rolls = (only_rolls < 5).sum() - (only_rolls == 0).sum()
		total_rolls += rolls
	return total_rolls

def p1(filename='example.txt'):
	return get_accessible_rolls(get_floorplan(filename))

def p2(filename='example.txt'):
	return get_accessible_rolls_p2(get_floorplan(filename))

print(p1('input.txt'))
print(p2('input.txt'))