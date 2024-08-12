#1. Cai dat thuat toan BFS
from collections import defaultdict
from queue import Queue, PriorityQueue

# read data from file txt
def read_txt(file):
	size = int(file.readline())
	start, goal = [int (num) for num in file.readline().split(' ')]
	matrix = [[int (num) for num in line.split(' ')] for line in file]
	return size, start, goal, matrix

#convert matrix to list-near
def convert_graph(a):
	adjList = defaultdict(list)
	for i in range (len(a)):
		for j in range(len(a[i])):
			if a[i][j] == 1:
				adjList[i].append(j)
	return adjList

def convert_graph_weight(a):
	adjList = defaultdict(list)
	for i in range(len(a)):
		for j in range(len(a[i])):
			if a[i][j] != 0:
				adjList[i].append((j, a[i][j]))
	return adjList


#1. Cai dat thuat toan BFS
def BFS(graph, start, end):
	visited = []
	frontier = Queue()

	#thêm node start vào frontier và visited
	frontier.put(start)

	#start không có node cha
	parent = dict()
	parent[start] = None

	path_found = False

	while True:
		if frontier.empty():
			raise Exception("No way Exception")
		current_node = frontier.get()
		visited.append(current_node)

		# Kiểm tra current_node có là end hay không
		if current_node == end:
			path_found = True
			break

		for node in graph[current_node]:
			if node not in visited:
				frontier.put(node)
				parent[node] = current_node
				visited.append(node)
	# Xây dựng đường đi
	path = []
	if path_found:
		path.append(end)
		while parent[end] is not None:
			path.append(parent[end])
			end = parent[end]
		path.reverse()
	return path

#2. Cai dat thuat toan DFS
def DFS(graph, start, end):
	visited = []
	frontier = []

	#Thêm node start vào frontier và visited
	frontier.append(start)

	#start không có node cha
	parent = dict()
	parent[start] = None

	path_found = False

	while True:
		if frontier == []:
			raise Exception("No way Exception")
		current_node = frontier.pop()
		visited.append(current_node)

		# Kiểm tra current_node có là end hay không
		if current_node == end:
			path_found = True
			break

		for node in graph[current_node]:
			if node not in visited:
				frontier.append(node)
				parent[node] = current_node
				visited.append(node)

	# Xây dựng đường đi
	path = []
	if path_found:
		path.append(end)
		while parent[end] is not None:
			path.append(parent[end])
			end = parent[end]
		path.reverse()
	return path

#3. Cài đặt thuật toán UCS


def UCS(graph, start, end):
	visited = []
	frontier = PriorityQueue()

	frontier.put((0, start))

	parent = dict()
	parent[start] = None

	path_found = False

	while True:
		if frontier.empty():
			raise Exception("No way Exception")
		current_w, current_node = frontier.get()
		visited.append(current_node)

		if current_node == end:
			path_found = True
			break

		for neighbor, cost in graph[current_node]:
			if neighbor not in visited:
				if neighbor not in [node for _, node in frontier.queue]:
					frontier.put(((current_w + cost), neighbor))
					parent[neighbor] = current_node
				else:
					for _, node in frontier.queue:
						if node == neighbor and current_w + cost < _:
							frontier.queue.remove((_, node))
							frontier.put(((current_w + cost), neighbor))
							parent[neighbor] = current_node

	path = []
	if path_found:
		while parent[end] is not None:
			path.append(parent[end])
			end = parent[end]
		path.reverse()
	return current_w, path

if __name__ == "__main__":
	#Đọc file Input.txt và InputUCS.txt
	file_1 = open("Input.txt","r")
	file_2 = open("InputUCS.txt","r")
	size_1, start_1, goal_1, matrix_1 = read_txt(file_1)
	size_2, start_2, goal_2, matrix_2 = read_txt(file_2)
	file_1.close()
	file_2.close()
	graph_1 = convert_graph(matrix_1)
	graph_2 = convert_graph_weight(matrix_2)

	#Thực thi thuật toán BFS
	result_bfs = BFS(graph_1, start_1, goal_1)
	print("Kết quả sử dụng thuật toán BFS: \n",result_bfs)
	#Thực thi thuật toán DFS
	result_dfs = DFS(graph_1, start_1, goal_1)
	print("Kết quả sử dụng thuật toán DFS: \n",result_dfs)
	#Thực thi thuật toán UCS
	cost, result_ucs = UCS(graph_2, start_2, goal_2)
	print("Kết quả sử dụng thuật toán UCS: \n",result_ucs,"với tổng chi phí là",cost)