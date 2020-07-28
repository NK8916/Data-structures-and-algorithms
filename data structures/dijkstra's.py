import math

class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.values = []

    def enqueue(self, val, priority):
        node = Node(val, priority)
        self.values.append(node)
        index = len(self.values) - 1
        parentindex = math.floor((index - 1) / 2)
        while self.values[parentindex].priority > self.values[index].priority and parentindex >= 0 and index >= 0:
            self.values[parentindex], self.values[index] = self.values[index], self.values[parentindex]
            index = parentindex
            parentindex = math.floor((index - 1) / 2)
        return self

    def dequeue(self):
        self.values[0], self.values[len(self.values) - 1] = self.values[len(self.values) - 1], self.values[0]
        item = self.values.pop()
        index = 0
        while True:
            node = None
            left = 2 * index + 1
            right = 2 * index + 2
            pos = index
            if left < len(self.values):
                if self.values[left].priority < self.values[index].priority:
                    node = self.values[left]
                    pos = left
            if right < len(self.values):
                if (not node and self.values[right].priority < self.values[index].priority) or (
                        node and node.priority > self.values[
                    right].priority):
                    node = self.values[right]
                    pos = right
            if node is None:
                break;
            self.values[pos] = self.values[index]
            self.values[index] = node
            index = pos

        return item

class WeightedGraph:
    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, vertex):
        if not self.adjacencyList.get(vertex):
            self.adjacencyList[vertex] = []
        return self

    def addEdge(self, vertex1, vertex2, weight):
        self.adjacencyList[vertex1].append({'node': vertex2, 'weight': weight})
        self.adjacencyList[vertex2].append({'node': vertex1, 'weight': weight})
        return self

    def dijkstras(self, start, end):
        distances = {}
        priorityQueue = PriorityQueue()
        previous = {}
        path = []
        for key in self.adjacencyList:
            previous[key] = None
            if key == start:
                distances[key] = 0
                priorityQueue.enqueue(key, 0)
            else:
                distances[key] = math.inf
                priorityQueue.enqueue(key, math.inf)
        while len(priorityQueue.values):
            current = priorityQueue.dequeue()
            if current.val == end:
                item = current.val
                while item:
                    path.insert(0,item)
                    item = previous[item]
                return path
            for value in self.adjacencyList[current.val]:
                dist = distances[current.val] + value['weight']
                if distances[value['node']] > dist:
                    distances[value['node']] = dist
                    previous[value['node']] = current.val
                    priorityQueue.enqueue(value['node'], dist)


weightedGraph = WeightedGraph()

weightedGraph.addVertex("A").addVertex("B").addVertex("C").addVertex("D").addVertex("E").addVertex("F")
weightedGraph.addEdge("A", "B", 4).addEdge("A", "C", 2).addEdge("B", "E", 3).addEdge(
    "C", "D", 2).addEdge("C", "F", 4).addEdge("D", "E", 3).addEdge("D", "F", 1).addEdge("E", "F", 1)
result = weightedGraph.dijkstras("A", "E")
print("Result: ", result)
