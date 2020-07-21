from collections import defaultdict
class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = defaultdict(list)

	# Function to add an edge in an undirected graph
	def add_edge(self, src, dest):
		self.graph[src].append(dest)
		self.graph[dest].append(src)

def BFS(n, vertex):
	lst = [0]*n
	queue = []
	queue.append(vertex)
	ans = []
	lst[vertex] = 1

	while(queue!=[]):
		x = queue.pop(0)
		ans.append(x)
		ar = g.graph[x]
		for i in ar:
			if lst[i] == 0:
				queue.append(i)
				lst[i] = 1
	return ans

t = 5
g = Graph(t)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

print(BFS(t, 0))