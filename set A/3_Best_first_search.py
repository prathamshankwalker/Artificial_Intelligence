# implement best first search using python#
from collections import defaultdict
from queue import PriorityQueue
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visual = []

    def addEdge(self, u, v,cost):
        self.graph[u].append((v,cost))
        self.visual.append((u,v))

    def visualizeGraph(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw(G, with_labels = True)
        plt.show() 

    def BestFirstSearch(self, source,target,n,heuristic):
        q = PriorityQueue()
        visited = [False] * (n+1)
        q.put((heuristic[source],source))
        visited[source] = True
        totalCost = 0
        
        while not q.empty():
            source = q.get()[1]

            print(source, end=" ")
            if source == target:
                break

            for i,cost in self.graph[source]:
                if visited[i] == False:
                    # print(i,heuristic[i])
                    q.put((heuristic[i],i))
                    visited[i] = True
    



g = Graph()

n = int(input("Enter the number of vertices:"))
type = int(input("Enter the type of graph\n1. Directed\n2. Undirected\n"))

if type == 1:
    maxNumberOFEdges = n*(n-1)
else:
    maxNumberOFEdges = (n*(n-1))//2

# graph input
for i in range(maxNumberOFEdges):
    print("Enter the edge and the cost", i+1, "(-1 -1 -1 to exit)")
    u, v, cost = map(int, input().split(" ",3))
    if u == -1 and v == -1:
        break
    g.addEdge(u, v,cost)
    if (type == 2):
        g.addEdge(v, u,cost)

heuristic = [0]*(n+1)
for i in range(n):
    heuristic[i] = int(input(f"Enter the heurstic values for node {i}: "))

source = int(input("\nEnter the source:"))
target = int(input("Enter the target:"))
print("Best First Search Traversal:",end=" ")
g.BestFirstSearch(source,target,n,heuristic)

g.visualizeGraph()