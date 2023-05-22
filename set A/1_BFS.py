# 1. write python program to implement BFS using python
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
"""
Example:
    1
  /  | \
 2  3  4
/ \/ \/ \
5 67 89 10  

"""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        x = self.queue.pop(0)
        return x

    def empty(self):
        if (len(self.queue) == 0):
            return True
        else:
            return False

    def printQueue(self):
        for element in self.queue:
            print(element, end=" ")

        print()


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printGraph(self):
        for key, value in self.graph.items():
            print(key, value)

    def visualizeGraph(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw(G, with_labels = True)
        plt.show() 

    def BFS(self, source,n):
        q = Queue()
        visited = [False] * (n+1)
        q.enqueue(source)
        visited[source] = True
        while not q.empty():
            source = q.dequeue()
            print(source, end=" ")

            for i in self.graph[source]:
                if visited[i] == False:
                    q.enqueue(i)
                    visited[i] = True
        print()

g = Graph()

n = int(input("Enter the number of vertices:"))
type = int(input("Enter the type of graph\n1. Directed\n2. Undirected\n"))

if type == 1:
    maxNumberOFEdges = n*(n-1)
else:
    maxNumberOFEdges = (n*(n-1))//2

for i in range(maxNumberOFEdges):
    print("Enter the edge", i+1, "(-1 -1 to exit)")
    u, v = map(int, input().split())
    if u == -1 and v == -1:
        break
    g.addEdge(u, v)
    if (type == 2):
        g.addEdge(v, u)
        
g.visualizeGraph()
source = int(input("\nEnter the source:"))
print("BFS Traversal:",end=" ")
g.BFS(source,n)

