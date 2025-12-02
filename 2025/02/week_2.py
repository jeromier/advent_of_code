import math

def check_valid_id(product_id):
	product_id = str(product_id)
	midpoint = len(product_id) // 2

	if len(product_id) % 2 != 0:
		return True
	elif product_id[:midpoint] == product_id[midpoint:]:
		return False
	else:
		return True

def check_id_range(beginning,end):
	print('Checking range from',beginning,'to',end)
	total = 0
	i = beginning

	# skip numbers that have an odd number of digits
	# they can't be invalid
	if len(str(i)) % 2 != 0:
		print('skipping from',i)
		i = 10 ** math.ceil(math.log10(i))
		print('to',i)

	while i <= end:
		if not check_valid_id(i):
			total += i
		i += 1
		# again, skip numbers with an odd number of digits
		if len(str(i)) % 2 != 0:
			print('skipping from',i)
			i = 10 ** math.ceil(math.log10(i))
			print('to',i)
	
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


