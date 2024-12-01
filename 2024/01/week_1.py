

def calculate_distance(list1, list2):
	list1.sort()
	list2.sort()
	total_distance = 0
	for i in range(len(list1)):
		total_distance += abs(list1[i] - list2[i])
	return total_distance

def similarity(list1, list2):
	list1.sort()
	list2.sort()
	similarity = 0
	for i in range(len(list1)):
		similarity += list1[i] * list2.count(list1[i])
	return similarity

def problem_1():
	with open('input.txt') as dataset:
		left_list = []
		right_list = []
		for line in dataset:
			values = line.split()
			left_list.append(int(values[0]))
			right_list.append(int(values[1]))
		print(calculate_distance(left_list,right_list))

def problem_2():
	with open('input.txt') as dataset:
		left_list = []
		right_list = []
		for line in dataset:
			values = line.split()
			left_list.append(int(values[0]))
			right_list.append(int(values[1]))
		print(similarity(left_list,right_list))

if __name__ == '__main__':
	problem_2()




