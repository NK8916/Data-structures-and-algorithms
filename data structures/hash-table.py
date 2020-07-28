class Hashmap:
    def __init__(self, size=53):
        self.keyMap = [None] * size

    def hash(self, key):
        total = 0
        prime = 31
        for i in range(0, min(len(key), 100)):
            total = (total * prime + ord(key[i]) - 96) % len(self.keyMap)

        return total

    def set(self, key, value):
        hashkey = self.hash(key)
        if not self.keyMap[hashkey]:
            self.keyMap[hashkey] = []
        self.keyMap[hashkey].append([key, value])
        return self

    def get(self, key):
        hashkey = self.hash(key)
        if not self.keyMap[hashkey]:
            return None
        else:
            for i in range(0, len(self.keyMap[hashkey])):
                if self.keyMap[hashkey][i][0] == key:
                    return self.keyMap[hashkey][i][1];
        return None

    def keys(self):
        result = []
        for i in range(0, len(self.keyMap)):
            if self.keyMap[i]:
                for j in range(0, len(self.keyMap[i])):
                    if self.keyMap[i][j][0] not in result:
                        result.append(self.keyMap[i][j][0])
        return result

    def values(self):
        result = []
        for i in range(0, len(self.keyMap)):
            if self.keyMap[i]:
                for j in range(0, len(self.keyMap[i])):
                    if self.keyMap[i][j][0] not in result:
                        result.append(self.keyMap[i][j][1])

        return result


hashmap = Hashmap()

hashmap.set('hello', 1).set('hi', 2).set('bye', 4).set('hello', 5)

print(hashmap.keyMap)

print("Get: ", hashmap.get('hello'))

print("Keys: ", hashmap.keys())

print("Values: ", hashmap.values())
