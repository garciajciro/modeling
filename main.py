 #Create adjacency matrix (from https://linuxtut.com/en/2a327fe021fb7dafe07a/)

# Open the txt file which shouldn't have any empty lines
with open("AdjList_emergency_Facilities (1).txt", "r") as l:
  # read the first line to the the n and m. First line should have 2 numbers
  n, m = map(int, l.readline().split())
  
  # Go through every line and get the numbers. Put in a list inside a list
  s = [list(map(int, l.readline().split())) for _ in range(m)]

adjacencyMatrix = [[0]*n for _ in range(n)]

for v in s:
  if v != []:
    adjacencyMatrix[v[0]-1][v[1]-1] = v[2]  #Here is changing
    adjacencyMatrix[v[1]-1][v[0]-1] = v[2]  #Erase if it is a directed graph
 
print(adjacencyMatrix)  # [[0, 1, 1, 0, 1], ..., [1, 0, 1, 0, 0]]

# From https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def printSolution(self, dist):
		with open("outputSources.txt", "a") as f:

			f.write("Vertex \t Distance from Source\n")
			for node in range(self.V):
				f.write(f"{node} \t\t\t {dist[node]}\n")

	# A utility function to find the vertex with
	# minimum distance value, from the set of vertices
	# not yet included in shortest path tree
	def minDistance(self, dist, sptSet):

		# Initialize minimum distance for next node
		min = 1e7

		# Search not nearest vertex not in the
		# shortest path tree
		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v

		return min_index

	# Function that implements Dijkstra's single source
	# shortest path algorithm for a graph represented
	# using adjacency matrix representation
	def dijkstra(self, src):

		dist = [1e7] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):

			# Pick the minimum distance vertex from
			# the set of vertices not yet processed.
			# u is always equal to src in first iteration
			u = self.minDistance(dist, sptSet)

			# Put the minimum distance vertex in the
			# shortest path tree
			sptSet[u] = True

			# Update dist value of the adjacent vertices
			# of the picked vertex only if the current
			# distance is greater than new distance and
			# the vertex in not in the shortest path tree
			for v in range(self.V):
				if (self.graph[u][v] > 0 and
				sptSet[v] == False and
				dist[v] > dist[u] + self.graph[u][v]):
					dist[v] = dist[u] + self.graph[u][v]

		self.printSolution(dist)

# Driver program
print(adjacencyMatrix)
g = Graph(66)
g.graph = adjacencyMatrix

#This creates various adjacency Matrix from all the sources
#in the adjancecy Matrix
for n in range(66):

	g.dijkstra(n)

#This creates a file that has
#The distance from the source to the other nodes
#Every time that the code is re-run the previous
#outputSources file should be deleted



# This code is contributed by Divyanshu Mehta
