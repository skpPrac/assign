def load_file(filename):
	input_arr = []
	with open(filename) as f:
		for line in f:
			input_arr.append(int(line.strip()))
	return input_arr


def qso(input_arr, l, r):
	if l < r:
		piv = partition(input_arr, l, r)
		return (r-l-1) + qso(input_arr, l, piv) + qso(input_arr, piv+1, r)
	return 0


def find_med(input_arr, l, r):
	mid = (l+r)/2
	if (input_arr[l] > input_arr[mid] and input_arr[l] < input_arr[r]) or (input_arr[l] < input_arr[mid] and input_arr[l] > input_arr[r]):
		return l
	elif (input_arr[mid] > input_arr[l] and input_arr[mid] < input_arr[r]) or (input_arr[mid] < input_arr[l] and input_arr[mid] > input_arr[r]):
		return mid
	elif (input_arr[r] > input_arr[mid] and input_arr[r] < input_arr[l]) or (input_arr[r] > input_arr[l] and input_arr[r] < input_arr[mid]):
		return r
	return -1


def swap(input_arr, l, r):
	temp = input_arr[r]
	input_arr[r] = input_arr[l]
	input_arr[l] = temp


def partition(input_arr, l, r):
	med_index = r-1
	if (r-1)-l > 1:
		med_index = find_med(input_arr, l, r-1)
	swap(input_arr, l, med_index)
	piv = input_arr[l]
	i = l+1
	for j in range(l+1, r):
		if input_arr[j] < piv:
			temp = input_arr[i]
			input_arr[i] = input_arr[j]
			input_arr[j] = temp
			i += 1
	input_arr[l] = input_arr[i-1]
	input_arr[i-1] = piv
	return i-1

a = load_file('input.txt')
#a = [5,3,7,2,8,1,4]
rec_calls = qso(a, 0, len(a))
print(a)
print(rec_calls)
