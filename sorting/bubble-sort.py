array = []


num = int(input('Enter the number of elements: '))

for i in range(0, num):
    ele = int(input())
    array.append(ele)

print(array)


def bubble_sort(array):
    for i in reversed(range(1, len(array))):
        swap = 0
        for j in range(0, i):
            if array[j + 1] < array[j]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap = 1
        if not swap:
            break

    return array


result = bubble_sort(array)

print("Result: ", result)
