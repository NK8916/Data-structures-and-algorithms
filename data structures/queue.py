class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, val):
        node = Node(val)
        if not self.first:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

        self.size += 1
        return self

    def dequeue(self):
        if not self.first:
            return None
        if self.size == 1:
            self.first = None
            self.last = None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None

        return self

    def traverse(self):
        current = self.first
        while current is not None:
            print("Value: ", current.val)
            current = current.next


queue = Queue()
queue.enqueue(23).enqueue(33).enqueue(44).enqueue(34).enqueue(66).enqueue(45)

queue.traverse()

queue.dequeue()
print("After DEQUEQUE: ")
queue.traverse()
