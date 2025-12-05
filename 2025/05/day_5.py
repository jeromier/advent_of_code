from itertools import chain

def contains(current_id, fresh_ids):
	for id_range in fresh_ids:
		if id_range[0] <= current_id <= id_range[1]:
			return True
	return False

def check_begin(current_id, fresh_ids):
	for id_range in fresh_ids:
		if id_range[0] <= current_id <= id_range[1]:
			return id_range[1] + 1
	return current_id

def check_end(current_id, fresh_ids):
	for id_range in fresh_ids:
		if id_range[0] <= current_id <= id_range[1]:
			return id_range[0] - 1
	return current_id

def get_fresh_ids(ingredients):
	fresh_ids = []
	line = ingredients.readline().strip()
	while line:
		fresh_ids.append([int(x) for x in line.split('-')])
		line = ingredients.readline().strip()
	return fresh_ids

def remove_contained_ranges(fresh_ids):
	new_fresh_ids = []
	
	for a in fresh_ids:
		contain = True
		for b in fresh_ids:
			if a[0] > b[0] and a[1] < b[1]:
				contain = False
				break
		if contain:
			new_fresh_ids.append(a)

	return new_fresh_ids


def get_non_overlapping_fresh_ids(ingredients):
	fresh_ids = []
	line = ingredients.readline().strip()
	while line:
		begin,end = [int(x) for x in line.split('-')]
		
		new_beginning = check_begin(begin, fresh_ids)
		while new_beginning != begin:
			begin = new_beginning
			new_beginning = check_begin(begin, fresh_ids)

		new_end = check_end(end, fresh_ids)
		while new_end != end:
			end = new_end
			new_end = check_end(end, fresh_ids)

		if begin <= end:
			fresh_ids.append([begin,end])
		line = ingredients.readline().strip()
	return fresh_ids


def p1(filename='example.txt'):
	with open(filename) as ingredients:
		fresh_ids = get_fresh_ids(ingredients)

		fresh_ingredients = 0
		line = ingredients.readline().strip()
		while line:
			if contains(int(line), fresh_ids):
				fresh_ingredients += 1
			line = ingredients.readline().strip()
	return fresh_ingredients

def p2(filename='example.txt'):
	with open(filename) as ingredients:
		fresh_ids = get_non_overlapping_fresh_ids(ingredients)
		# print(fresh_ids)
		fresh_ids = remove_contained_ranges(fresh_ids)
		# print(fresh_ids)

		total_fresh_ids = 0
		for id_range in fresh_ids:
			total_fresh_ids += id_range[1] - id_range[0] + 1
		return total_fresh_ids





#print(p1('input.txt'))
print(p2('input.txt'))