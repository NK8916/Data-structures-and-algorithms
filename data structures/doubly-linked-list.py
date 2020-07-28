class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Doublylinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

        return self

    def pop(self):
        temp = self.tail
        if not self.head:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            self.tail = self.tail.prev
            self.tail.next.prev = None
            self.tail.next = None

        self.length -= 1

        return temp

    def shift(self):
        temp = self.head
        if not self.head:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev.next = None
            self.head.prev = None
        self.length -= 1
        return temp

    def unshift(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1

        return self

    def get(self, pos):
        if pos <= 0 or pos > self.length:
            return None
        else:
            mid = int(self.length / 2)
            element = None
            if pos <= mid:
                i = 1
                current = self.head
                while i <= mid:
                    if pos == i:
                        element = current
                    current = current.next
                    i += 1

            if pos > mid:
                i = self.length
                current = self.tail
                while i > mid:
                    if pos == i:
                        element = current
                    current = current.prev
                    i -= 1
            return element

    def set(self, pos, val):
        node = self.get(pos)
        if not node:
            return False
        else:
            node.val = val
            return True

    def insert(self, pos, val):
        if pos <= 0 or pos > self.length:
            return False
        else:
            node = Node(val)
            prev_node = self.get(pos - 1)
            node.next = prev_node.next
            prev_node.next.prev = node
            node.prev = prev_node
            prev_node.next = node
            self.length += 1
            return True

    def remove(self, pos):
        if pos <= 0 or pos > self.length:
            return None
        else:
            node = self.get(pos)
            temp = node
            node.prev.next = node.next
            node.next.prev = node.prev
            node.nest = None
            node.prev = None
            return temp

    def reverse(self):
        self.head, self.tail = self.tail, self.head
        prev_pointer = self.tail
        current = self.tail.next
        self.tail.next = None
        while current is not None:
            next_pointer = current.next
            current.prev = current.next
            current.next = prev_pointer
            prev_pointer.prev = current
            prev_pointer = current
            current = next_pointer

    def traverse(self):
        pointer = self.head
        while pointer is not None:
            print("Value: ", pointer.val)
            pointer = pointer.next


doublylinkedlist = Doublylinkedlist()

doublylinkedlist.push(23).push(33).push(34).push(44).push(55).push(60).push(60).push(65).push(21)

doublylinkedlist.traverse()

doublylinkedlist.pop()
print("After POP: ")
doublylinkedlist.traverse()

doublylinkedlist.shift()
print("After SHIFT: ")
doublylinkedlist.traverse()

doublylinkedlist.unshift(99)
print("After UNSHIFT: ")
doublylinkedlist.traverse()

item = doublylinkedlist.get(5)
print("After GET: ", item.val)

doublylinkedlist.set(6, 100)
print("After Set: ")
doublylinkedlist.traverse()

doublylinkedlist.insert(4, 121)
print("After Insert: ")
doublylinkedlist.traverse()

doublylinkedlist.remove(5)
print("After Remove: ")
doublylinkedlist.traverse()

doublylinkedlist.reverse()
print("Reverse: ")
doublylinkedlist.traverse()
