import time

start_time = time.time()


class Compute(object):

	def __init__(self):
		self.forward_list = []
		self.rev_dict = {}
		self.forward_dict = {}

	def read_file(self, filename):
		with open(filename) as f:
			lines = f.readlines()
			for line in lines:
				temp = line.split()
				one = int(temp[0])
				two = int(temp[1])
				self._build_dict(self.rev_dict, two, one)
				self.forward_list.append([one, two])

	def _build_dict(self, dict_to_modify, one, two):
		vals = dict_to_modify.get(one)
		if vals:
			vals.append(two)
			dict_to_modify[one] = vals
		else:
			dict_to_modify[one] = [two]

	def dfs_iter(self, input_dict, i):
		stack = [i]
		while stack:
			value = stack[len(stack)-1]
			self.leader[value] = self.s
			self.visited[value] = value
			if input_dict.get(value):
				flag = 0
				for val in input_dict[value]:
					if not self.visited.get(val):
						flag = 1
						self.visited[val] = val
						stack.append(val)
				if flag == 0:
					self.t += 1
					self.f[value] = self.t
					stack.pop()
			else:
				self.t += 1
				self.f[value] = self.t
				stack.pop()

	def dfs(self, input_dict, i):
		self.visited[i] = i
		self.leader[i] = self.s
		if input_dict.get(i):
			for val in input_dict[i]:
				if not self.visited.get(val):
					self.dfs(input_dict, val)
		self.t += 1
		self.f[i] = self.t

	def dfs_loop(self, input_dict):
		self.t = 0
		self.s = None
		self.visited = {}
		self.leader = {}
		self.f = {}
		for i in range(875714, 0, -1):
			if not self.visited.get(i):
				self.s = i
				# self.dfs(input_dict, i)
				self.dfs_iter(input_dict, i)

	def _replace_nodes(self):
		for edge in self.forward_list:
			edge = [self.f[edge[0]], self.f[edge[1]]]
			self._build_dict(self.forward_dict, edge[0], edge[1])

	def main(self):
		self.read_file('input.txt')
		print('--- {} seconds ---'.format(time.time() - start_time))
		self.dfs_loop(self.rev_dict)
		# print('visited: ', self.visited)
		# print('f: ', self.f)
		self._replace_nodes()
		# print('forward_dict: ', self.forward_dict)
		self.dfs_loop(self.forward_dict)
		# print('leaders: ', self.leader)
		leaders_dict = {}
		for val in sorted(self.leader.values()):
			count = leaders_dict.get(val)
			if count:
				leaders_dict[val] = count+1
			else:
				leaders_dict[val] = 1
		print(sorted(leaders_dict.values(), reverse=True)[:5])


Compute().main()
print('--- {} seconds ---'.format(time.time() - start_time))
