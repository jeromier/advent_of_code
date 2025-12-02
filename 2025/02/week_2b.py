import math

def check_valid_id(product_id):
	product_id = str(product_id)
	midpoint = len(product_id) // 2 + 1

	for i in range(1,midpoint):
		# only check substring lengths that evenly
		# divide the number
		if len(product_id) % i != 0:
			continue
		
		if product_id[:i] * (len(product_id) // i) == product_id:
			# print('invalid id',product_id)
			return False

	return True


def check_id_range(beginning,end):
	print('Checking range from',beginning,'to',end)
	total = 0
	i = beginning

	while i <= end:
		if not check_valid_id(i):
			total += i
		i += 1	
	
	return total

def check_all_ids(filename='example.txt'):
	total = 0

	with open(filename) as id_file:
		id_list = id_file.read().strip().split(',')
		for item in id_list:
			beginning, end = [int(n) for n in item.split('-')]
			total += check_id_range(beginning, end)

	return total

print(check_all_ids('input.txt'))


