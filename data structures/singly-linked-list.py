class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
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
            self.tail = node
        self.length += 1
        return self

    def pop(self):
        pointer = self.head
        prev_pointer = self.head
        if not self.head:
            return None
        while pointer != self.tail:
            prev_pointer = pointer
            pointer = pointer.next
        prev_pointer.next = None
        self.tail = prev_pointer
        self.length -= 1
        return pointer.val

    def shift(self):
        if not self.head:
            return None
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        return temp.val

    def unshift(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        node.next = self.head
        self.head = node
        self.length += 1
        return self

    def get(self, pos):
        if pos < 0 or pos > self.length:
            return False
        pointer = self.head
        current = 0
        while current != pos:
            pointer = pointer.next
            current += 1
        return pointer

    def set(self, pos, value):
        node = self.get(pos)
        if node:
            node.val = value
            return True
        return False

    def insert(self, pos, value):
        if pos < 0 or pos > self.length:
            return False
        if pos == self.length:
            self.push(value)

        if pos == 0:
            self.unshift(value)
        else:
            node = Node(value)
            prev_node = self.get(pos - 1)
            node.next = prev_node.next
            prev_node.next = node
        self.length += 1
        return self

    def remove(self, pos):
        if pos == self.length - 1:
            self.pop()
        if pos == 0:
            self.shift()
        else:
            prev_node = self.get(pos - 1)
            prev_node.next = prev_node.next.next
        self.length -= 1
        return self

    def reverse(self):
        self.head, self.tail = self.tail, self.head
        prev_pointer = self.tail
        current = self.tail.next
        self.tail.next = None
        while current is not None:
            next_pointer = current.next
            current.next = prev_pointer
            prev_pointer = current
            current = next_pointer

        return self

    def traverse(self):
        pointer = self.head
        while pointer != self.tail.next:
            print("Value: ", pointer.val)
            pointer = pointer.next


singlyLinkedList = SinglyLinkedList()

singlyLinkedList.push(23).push(33).push(55).push(34).push(45).push(44)

singlyLinkedList.traverse()

print("POP: ", singlyLinkedList.pop())
print("After POP: ")
singlyLinkedList.traverse()

print("SHIFT: ", singlyLinkedList.shift())
print("After SHIFT: ")
singlyLinkedList.traverse()

singlyLinkedList.unshift(88)
print("AFTER UNSHIFT: ")
singlyLinkedList.traverse()

print("Element at pos: ", singlyLinkedList.get(2).val)

print("After set: ")
singlyLinkedList.set(2, 98)
singlyLinkedList.traverse()

print("After Insert: ")
singlyLinkedList.insert(3, 100)
singlyLinkedList.traverse()

print("After Remove: ")
singlyLinkedList.remove(3)
singlyLinkedList.traverse()

singlyLinkedList.reverse()
print("After Reverse: ")
singlyLinkedList.traverse()
