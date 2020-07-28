class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class Binarysearchtree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            print("Root: ", self.root.value)
        else:
            current = self.root
            while True:
                if current.value < value:
                    if current.right:
                        current = current.right
                        continue
                    else:
                        current.right = node
                        print("Right: ", current.right.value)
                        break
                if current.value > value:
                    if current.left:
                        current = current.left
                        continue
                    else:
                        current.left = node
                        print("Left: ", current.left.value)
                        break
        return self

    def find(self, value):
        if not self.root:
            return False
        else:
            current = self.root
            while True:
                if current.value == value:
                    return True
                elif current.value < value:
                    if current.right:
                        current = current.right
                        continue
                    else:
                        return False
                elif current.value > value:
                    if current.left:
                        current = current.left
                        continue
                    else:
                        return False

    def BFS(self):
        if not self.root:
            return None
        else:
            queue = []
            visited = []
            queue.append(self.root)
            while len(queue):
                node = queue.pop(0)
                visited.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return visited

    def DFS_Preorder(self):
        visited = []
        current = self.root

        def preorder(current):
            visited.append(current.value)
            if current.left:
                preorder(current.left)
            if current.right:
                preorder(current.right)

        preorder(current)
        return visited

    def DFS_Postorder(self):
        visited = []
        current = self.root

        def postorder(current):
            if current.left:
                postorder(current.left)
            if current.right:
                postorder(current.right)
            visited.append(current.value)

        postorder(current)
        return visited

    def DFS_Inorder(self):
        visited = []
        current = self.root

        def inorder(current):
            if current.left:
                inorder(current.left)
            visited.append(current.value)
            if current.right:
                inorder(current.right)

        inorder(current)
        return visited


binarysearchtree = Binarysearchtree()
binarysearchtree.insert(23).insert(44).insert(21).insert(33).insert(66).insert(11).insert(22).insert(88)
print("Result")
elementNode = binarysearchtree.find(99)
print("Find: ", elementNode)

bfsResult = binarysearchtree.BFS()
for i in range(0, len(bfsResult)):
    print("Value: ", bfsResult[i].value)

print("DFS-preorder: ", binarysearchtree.DFS_Preorder())

print("DFS-postorder: ", binarysearchtree.DFS_Postorder())

print("DFS-inorder: ", binarysearchtree.DFS_Inorder())
