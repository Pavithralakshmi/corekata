from collections import defaultdict
class Graph:
  def __init__(self,vertices):
	  self.V = vertices 
		self.V_org = vertices
		self.graph = defaultdict(list) 
	def addEdge(self,u,v,w):
		if w == 1:
			self.graph[u].append(v)
		else: 
			self.graph[u].append(self.V)
			self.graph[self.V].append(v)
			self.V = self.V + 1
	def printPath(self, parent, j):
		Path_len = 1
		if parent[j] == -1 and j < self.V_org : 
			print j,
			return 0  
		l = self.printPath(parent , parent[j])
		Path_len = l + Path_len
	if j < self.V_org : 
			print j,

		return Path_len
def findShortestPath(self,src, dest):
	visited =[False]*(self.V)
	parent =[-1]*(self.V)
	queue=[]
  queue.append(src)
	visited[src] = True
	while queue :
  	s = queue.pop(0)
		if s == dest:
			return self.printPath(parent, s)
		for i in self.graph[s]:
			if visited[i] == False:
				queue.append(i)
				visited[i] = True
				parent[i] = s
g = Graph(4)
g.addEdge(0, 1, 2)
g.addEdge(0, 2, 2)
g.addEdge(1, 2, 1)
g.addEdge(1, 3, 1)
g.addEdge(2, 0, 1)
g.addEdge(2, 3, 2)
g.addEdge(3, 3, 2)

src = 0; dest = 3
print ("Shortest Path between %d and %d is " %(src, dest)),
l = g.findShortestPath(src, dest)
print ("\nShortest Distance between %d and %d is %d " %(src, dest, l)),
