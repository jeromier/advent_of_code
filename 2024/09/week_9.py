def expand_data(data):
	expanded_data = []
	for i in range(0,len(data),2):
		expanded_data += [str((i//2))] * int(data[i])

		if i+1 < len(data):
			empty_blocks = int(data[i+1])
		else:
			empty_blocks = 0

		expanded_data += ['.'] * empty_blocks

	return expanded_data

def fill_space(data):

	front_pointer = 0
	back_pointer = len(data)-1
	while front_pointer < back_pointer:
		if data[front_pointer] != '.': # advance until we find an empty space
			front_pointer += 1
		else:
			# find the next number at the back
			while data[back_pointer] == '.':
				back_pointer -= 1
			if back_pointer > front_pointer:
				data[front_pointer] = data[back_pointer]
				data[back_pointer] = '.'
				back_pointer -= 1

	# print(front_pointer,data[front_pointer],back_pointer,data[back_pointer])
	return data[:front_pointer+1]


def expand_data_for_part2(data):
	expanded_data = []
	for i in range(0,len(data),2):

		expanded_data.append( [str((i//2)),int(data[i])])

		if i+1 < len(data):
			empty_blocks = int(data[i+1])
		else:
			empty_blocks = 0

		expanded_data.append(empty_blocks)

	return expanded_data

def fill_space_without_fragmentation(data):
	back_pointer = len(data) - 2 # pointing to last data element
	end_point = 0 

	while back_pointer > end_point:
		front_pointer = 1
		# find the next spot big enough for the last data element
		# print('looking for a spot for file',data[back_pointer][0])
		while front_pointer < back_pointer:
			if data[front_pointer] >= data[back_pointer][1]:
				# print('found it at',front_pointer)
				data[front_pointer] -= data[back_pointer][1]
				data[back_pointer-1] += data[back_pointer][1] + data[back_pointer+1]
				data_block = data.pop(back_pointer)
				data.pop(back_pointer)

				data.insert(front_pointer,data_block)
				data.insert(front_pointer,0)
				back_pointer += 2
				end_point += 2

				break

			front_pointer += 2
		back_pointer -= 2


	return data

def check_sum_part_2(data):
	total = 0
	data_index = 0

	i = 0
	while i < len(data):
		block_value = int(data[i][0])
		num_blocks = data[i][1]

		for j in range(data_index,data_index + num_blocks):
			total += j * block_value

		data_index += num_blocks
		data_index += data[i+1]
		i+=2
	return total


def check_sum(data):
	total = 0

	i = 0
	while data[i] != '.':
		total += i * int(data[i])
		i+=1
	return total



def problem_1():
	""" Do something
	"""
	with open('input.txt') as dataset:
		data = dataset.read().strip()

		expanded_data = expand_data(data)

		filled_data = fill_space(expanded_data)
		# print(defragged_data)
		
		total = check_sum(filled_data)
		return total

def problem_2():
	""" Do something
	"""
	with open('input.txt') as dataset:
		data = dataset.read().strip()

		expanded_data = expand_data_for_part2(data)
		# print(expanded_data)
		compact_data = fill_space_without_fragmentation(expanded_data)
		# print(len(compact_data))

		result = check_sum_part_2(compact_data)

		return result

if __name__ == '__main__':
	# print(problem_1())
	print(problem_2())
	