# write python program to demostrate dfs# Write a Python program to implement DFS using python data structure (For graph)
"""
Example:
    1
  / | \
 2  3  4
/ \/ \/ \
5 67 89 10  
"""

from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()
        
    def empty(self):
        if (len(self.stack) == 0):
            return True
        else:
            return False

    def printStack(self):
        for element in self.stack:
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

    def DFS(self, source,n):
        stack = Stack()
        visited = [False] * (n+1)
        stack.push(source)

        while not stack.empty():
            source = stack.pop()

            if not visited[source]:
                print(source, end=" ")
                visited[source] = True
            
            for i in self.graph[source]:
                if not visited[i]:
                    stack.push(i)
        
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

source = int(input("\nEnter the source:"))
print("DFS Traversal:",end=" ")
g.DFS(source,n)
