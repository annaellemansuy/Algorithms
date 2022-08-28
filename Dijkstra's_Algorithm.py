# breadthfirstsearch finds fewest segments, dijkstra's find fastest path
#Dijkstra finds path with the total smallest weight
#Each path is weighted
#step 1 : find node u can get to in the least amount of time
#step 2 : check if there's a cheaper path to the neighbours of this node, if so update costs
#step 3 : Repeat until we've done for every node in graph
#step 4 : Calculate final path
# only works for directed acrylic graphs
# for example if you have negative weight edges (for example if you lose weight (negative) while going to the node) then Dijkstra's algorithm doesn't work
#To find negative weighted edges you need to use Bellman-Ford Algorithm

#new scenario: You are trying to buy a rolls royce from your friends priced the same
# However you need to take into account the travel costs of going to your friend to buy the rolls royce\



from queue import PriorityQueue


## Graph class implemented using adjacency list
class Graph:
	# Constructor
	def __init__(self):
		self.adj_list = {}

	# Add edge to the graph
	def add_edge(self,node1,node2,weight=1):
		if node1 not in self.adj_list.keys():
			self.adj_list[node1] = set()
		if node2 not in self.adj_list.keys():
			self.adj_list[node2] = set()
		self.adj_list[node1].add((node2,weight))	

	# Display graph
	def display(self):
		for key in self.adj_list.keys():
			print('edge {} : {}'.format(key,self.adj_list[key]))



## Dijkstra's algorithm
def dijkstra(graph: Graph,start,end):
	## Initialize the priority queue
	pq = PriorityQueue()
	pq.put((0,start))
	## Initialize the distance array
	dist = {}
	for node in graph.adj_list.keys():
		dist[node] = float('inf')
	dist[start] = 0
	## Initialize the parent array
	parent = {}
	for node in graph.adj_list.keys():
		parent[node] = None
	## Initialize the visited array
	visited = {}
	for node in graph.adj_list.keys():
		visited[node] = False
	## Initialize the path dictionary
	path = {}
	while not pq.empty():
		## Get the node with the minimum distance
		dist_node,node = pq.get()
		## Mark the node as visited
		visited[node] = True
		## Update the distance of the adjacent nodes
		for adj_node in graph.adj_list[node]:
			if not visited[adj_node[0]]:
				if dist[node] + adj_node[1] < dist[adj_node[0]]:
					dist[adj_node[0]] = dist[node] + adj_node[1]
					parent[adj_node[0]] = node
					pq.put((dist[adj_node[0]],adj_node[0]))
	## Get the path
	node = end
	while node != start:
		path[node] = parent[node]
		node = parent[node]
	return dist[end],path


def display_path(path, start, end):
	str = ''
	node = end
	while node != start:
		str = ' -> ' + node + str
		node = path[node]
	str = start + str
	return str


graph = Graph()
graph.add_edge("Paris","Verdun",100)
graph.add_edge("Paris","Lyon",500)
graph.add_edge("Lyon","Marseille",400)
graph.add_edge("Lyon","Grenoble",400)
graph.add_edge("Verdun","Grenoble",200)


graph.display()


start = "Paris"
end = "Grenoble"

distance,path = dijkstra(graph, start, end)
printable_path = display_path(path, start, end)



print("Path from {} to {} : {}. Distance {}".format(start,end,printable_path,distance))

print(path)

