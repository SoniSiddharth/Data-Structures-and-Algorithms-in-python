from collections import defaultdict
class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = defaultdict(list)

	# Function to add an edge in an undirected graph
	def add_edge(self, src, dest):
		self.graph[src].append(dest)
		self.graph[dest].append(src)

def DFS(n, vertex):
	lst = [0]*n
	queue = []
	queue.append(vertex)
	lst[vertex] = 1
	ans = []
	ans.append(vertex)
	while(queue!=[]):
		temp = 0
		x = queue[-1]
		for j in g.graph[x]:
			if lst[j]==0:
				lst[j] = 1
				ans.append(j)
				queue.append(j)
				temp = 1
				break
		if temp==0:
			queue.pop()
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

print(DFS(t, 0))
