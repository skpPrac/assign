import random


def read_file(input_file):
	input_dict = {}
	with open(input_file) as f:
		lines = f.readlines()
		for line in lines:
			edges = line.split()
			input_dict.update({int(edges[0]): [int(i) for i in edges[1:]]})
	return input_dict


def driver(input_dict):
	while len(input_dict) > 2:
		first_vertex = random.choice(list(input_dict.keys()))
		if input_dict.get(first_vertex):
			second_vertex = random.choice(input_dict[first_vertex])
			if input_dict.get(second_vertex):
				# add second_vertex elements to first_vertex 
				input_dict[first_vertex].extend(input_dict[second_vertex])

				# replace second_vertex value to be first_vertex
				nodes_to_update = input_dict[second_vertex]
				for node in nodes_to_update:
					input_dict[node] = [first_vertex if x==second_vertex else x for x in input_dict[node]]

				# remove self loops
				input_dict[first_vertex] = [x for x in input_dict[first_vertex] if x != first_vertex]

				# remove second_vertex
				input_dict.pop(second_vertex)

	print(input_dict)
	return [len(val) for val in input_dict.values()]


input_dict = read_file('input.txt')
print(driver(input_dict))
