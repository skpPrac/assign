def load_file(filename):
	input_arr = []
	with open(filename) as f:
		for line in f:
			input_arr.append(int(line.strip()))
	return input_arr


def mer(in_ar):
	if len(in_ar) < 2:
		return in_ar, 0
	elif len(in_ar) == 2:
		if in_ar[0] > in_ar[1]:
			return [in_ar[1], in_ar[0]], 1
		return in_ar, 0
	else:
		left,l_count = mer(in_ar[:(len(in_ar)/2)])
		right,r_count = mer(in_ar[len(in_ar)/2:])
		i = 0
		j = 0
		merge_count = 0
		ret_ar = []
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				ret_ar.append(left[i])
				i += 1
			else:
				merge_count += len(left) - i
				ret_ar.append(right[j])
				j += 1
		while i < len(left):
			ret_ar.append(left[i])
			i += 1
		while j < len(right):
			ret_ar.append(right[j])
			j += 1
		return ret_ar, l_count+r_count+merge_count

a = load_file('input.txt')
#print(a)
#a = [3,5,2,9,6,4]
print(mer(a))
