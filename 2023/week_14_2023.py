def shift_row_north(current_row,previous_row):
	for i in range(0,len(current_row)):
			if current_row[i] == 'O' and previous_row[i] == '.':
				previous_row[i] = 'O'
				current_row[i] = '.'

def tilt_north(platform):
	# Shift platform north
	for i in range(1,len(platform)):
		for j in range(i,0,-1): 
			shift_row_north(platform[j], platform[j-1])

def calc_load(platform):
	total_load = 0
	row_count = 0
	for row in platform:
		total_load += row.count('O') * (len(platform) - row_count)
		row_count += 1
	return total_load



if __name__ == '__main__':
	with open('input.txt') as dataset:
		platform = [list(x.strip()) for x in dataset.readlines()]

		tilt_north(platform)

		total_load = calc_load(platform)
		print(total_load)


