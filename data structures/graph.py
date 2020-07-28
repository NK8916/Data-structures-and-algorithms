class Graph:
    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, vertex):
        if not self.adjacencyList.get(vertex):
            self.adjacencyList[vertex] = []
        return self

    def addEdge(self, vertex1, vertex2):
        if not self.adjacencyList.get(vertex1):
            self.addVertex(vertex1)
        if not self.adjacencyList.get(vertex2):
            self.addVertex(vertex2)
        self.adjacencyList[vertex1].append(vertex2)
        self.adjacencyList[vertex2].append(vertex1)

        return self

    def removeEdge(self, vertex1, vertex2):
        if self.adjacencyList.get(vertex1):
            self.adjacencyList[vertex1].remove(vertex2)
        if self.adjacencyList.get(vertex2):
            self.adjacencyList[vertex2].remove(vertex1)
        return self

    def removeVertex(self, vertex):
        if self.adjacencyList.get(vertex):
            while len(self.adjacencyList[vertex]) is not 0:
                self.removeEdge(vertex, self.adjacencyList[vertex][0])
            del self.adjacencyList[vertex]
        return self

    def DFSRecursive(self, vertex):
        result = []
        visited = {}

        def DFSHelper(vertex):
            if not self.adjacencyList.get(vertex):
                return
            visited[vertex] = True
            result.append(vertex)
            for value in self.adjacencyList[vertex]:
                if not visited.get(value):
                    DFSHelper(value)
                if not visited[value]:
                    DFSHelper(value)

        DFSHelper(vertex)
        return result

    def DFSIterative(self, vertex):
        stack = []
        result = []
        visited = {}
        stack.append(vertex)
        visited[vertex] = True
        print("res: ", stack)
        while len(stack):
            print("in")
            item = stack.pop()
            result.append(item)
            for value in self.adjacencyList[item]:
                if not visited.get(value):
                    visited[value] = True
                    stack.append(value)

        return result

    def BFS(self, vertex):
        queue = []
        result = []
        visited = {}
        visited[vertex] = True
        queue.append(vertex)
        while len(queue):
            item = queue.pop(0)
            result.append(item)
            for value in self.adjacencyList[item]:
                if not visited.get(value):
                    visited[value] = True
                    queue.append(value)

        return result


graph = Graph()

graph.addVertex("A").addVertex("B").addVertex("C").addVertex("D").addVertex("E").addVertex("F")

graph.addEdge("A", "B").addEdge("A", "C").addEdge("B", "D").addEdge("C", "E").addEdge(
    "D", "E").addEdge("D", "F").addEdge("E", "F")

print("Result: ", graph.adjacencyList)

graph.removeEdge("edge2", "edge3")

print("Result after removal of edge: ", graph.adjacencyList)

graph.removeVertex("edge2")

print("Result after removal of vertex: ", graph.adjacencyList)

resultDFSRec = graph.DFSRecursive("A")
print("DFS Recursive: ", resultDFSRec)

resultDFSItv = graph.DFSIterative("A")
print("DFS Iterative: ", resultDFSItv)

resultBFS = graph.BFS("A")
print("Result BFS: ", resultBFS)
