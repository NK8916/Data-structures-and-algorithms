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
            # print("In Loop node: ", node.val)
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
            print("node: ", node.val)

        return item

    def print(self):
        for i in range(0, len(priorityQueue.values)):
            print("Result: Value: ", self.values[i].val, "Priority: ", self.values[i].priority)


priorityQueue = PriorityQueue()
priorityQueue.enqueue(35, 5).enqueue(32, 6).enqueue(44, 3).enqueue(55, 7).enqueue(34, 2).enqueue(30, 8).enqueue(20,
                                                                                                                4).enqueue(
    27, 1).enqueue(35, 9)

priorityQueue.print()

priorityQueue.dequeue()

print("After Dequeue: ")

priorityQueue.print()
