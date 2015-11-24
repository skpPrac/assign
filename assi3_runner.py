from assi_3 import driver, read_file


def run_it():
	least_val = 0
	for i in range(0, 1000):
		input_dict = read_file('input.txt')
		return_list = driver(input_dict)
		print('**********', return_list)
		if return_list[0] != return_list[1]:
			return -1
		if return_list[0] < least_val or least_val == 0:
			least_val = return_list[0]
	return least_val


print('$$$$$$$', run_it())
