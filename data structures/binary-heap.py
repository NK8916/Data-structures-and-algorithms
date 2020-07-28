import math


class MaxBinaryHeap:
    def __init__(self):
        self.values = []

    def insert(self, value):
        self.values.append(value)
        index = len(self.values) - 1
        parentindex = math.floor((index - 1) / 2)
        while self.values[parentindex] < self.values[index] and parentindex >= 0 and index >= 0:
            self.values[parentindex], self.values[index] = self.values[index], self.values[parentindex]
            index = parentindex
            parentindex = math.floor((index - 1) / 2)
        return self

    def extractMax(self):
        self.values[0], self.values[len(self.values) - 1] = self.values[len(self.values) - 1], self.values[0]
        item = self.values.pop()
        index = 0

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            pos = None
            if left < len(self.values):
                if self.values[left] > self.values[index]:
                    pos = left
            if right < len(self.values):
                if (not pos and self.values[right] > self.values[index]) or (
                        pos and self.values[pos] < self.values[
                    right]):
                    pos = right
            if pos is None:
                break;
            element=self.values[pos]
            self.values[pos] = self.values[index]
            self.values[index] = element
            index = pos
        return item


maxBinaryHeaps = MaxBinaryHeap()
maxBinaryHeaps.insert(35).insert(33).insert(42).insert(10).insert(14).insert(19).insert(27).insert(44).insert(
    26).insert(31)

print('Result: ', maxBinaryHeaps.values)

maxitem = maxBinaryHeaps.extractMax()
print("Item: ", maxitem)
print("After ExtractMax: ", maxBinaryHeaps.values)
