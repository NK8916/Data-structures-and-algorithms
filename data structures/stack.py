class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, val):
        node = Node(val)
        if not self.first:
            self.first = node
            self.last = node
        else:
            node.next = self.first
            self.first = node
        self.size += 1

        return self

    def pop(self):
        if not self.first:
            return None
        if self.size == 1:
            self.first = None
            self.last = None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
        self.size -= 1
        return self

    def traverse(self):
        current = self.first
        while current is not None:
            print("Value: ", current.val)
            current = current.next


stack = Stack()
stack.push(23).push(33).push(55).push(34).push(45).push(44)

stack.traverse()

stack.pop()
print("After POP: ")
stack.traverse()
