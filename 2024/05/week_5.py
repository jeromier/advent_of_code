import time

def update_is_valid(print_update, rules):
	""" Tests if the pages in the update follow
		the ordering rules
	"""
	print_update = print_update.copy()
	print_update.reverse() # reverse the update so I can check from the back first
	
	for i, page in enumerate(print_update):
		if page in rules:
			# if any page that should come after this one is actually
			# before it, the update is not valid
			if any(later_page in print_update[i+1:] for later_page in rules[page]):
				return False
	return True

def rightmost(pages, rules):
	""" The rightmost page will have no
		rules that require a page to come before it
	"""
	for page in pages:
		if page not in rules:
			return page
		else:
			if not any(later_page in pages for later_page in rules[page]):
				return page

def fix_update(print_update,rules):
	ordered_pages = []

	while len(print_update) > 0:
		right_page = rightmost(print_update,rules)
		ordered_pages.insert(0,right_page)
		print_update.remove(right_page)

	return ordered_pages


def get_rules(dataset):
	""" Creates a dictionary that shows which pages 
		need to come after any given page
	"""
	rules = {}
	for line in dataset:
		# get rules first
		if '|' in line:
			p1, p2 = [int(x) for x in line.split('|')]
			if p1 not in rules:
				rules[p1] = [p2]
			else:
				rules[p1].append(p2)
		else:
			return rules

def problem_1():
	""" Find correctly ordered updates
	"""
	total = 0
	with open('input.txt') as dataset:
		# get rules first
		rules = get_rules(dataset)

		for line in dataset:
			print_update = [int(x) for x in line.split(',')]
			
			if update_is_valid(print_update,rules):
				total += print_update[len(print_update)//2]

		return total

def problem_2():
	""" Reorder incorrectly ordered updates
	"""
	total = 0
	with open('input.txt') as dataset:
		# get rules first
		rules = get_rules(dataset)

		for line in dataset:
			print_update = [int(x) for x in line.split(',')]
			
			if not update_is_valid(print_update,rules):
				print_update = fix_update(print_update,rules)
				total += print_update[len(print_update)//2]


		return total

if __name__ == '__main__':
	# print(problem_1())
	print(problem_2())

	