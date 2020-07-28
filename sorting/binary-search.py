array = []
num = int(input('Enter the number of elements: '))

for i in range(0, num):
    ele = int(input())
    array.append(ele)

array.sort()
print(array)
item = int(input('Enter the item: '))

left = 0
right = len(array)-1


def binary_search(array, item, left, right):
    middle = int((left + right) / 2)

    print("middle ", middle)
    print("array",array)
    if left > right:
        return -1

    if item == array[middle]:
        print("result ", array[middle])
        return middle

    if item > array[middle]:
        left = middle + 1
        print("left", left)
        return binary_search(array, item, left, right)

    if item < array[middle]:
        right = middle - 1
        print("right", right)
        return binary_search(array, item, left, right)


result = binary_search(array, item, left, right)

print("Result: ", result)
