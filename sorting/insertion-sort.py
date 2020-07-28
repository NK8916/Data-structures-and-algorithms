array = []

num = int(input('Enter the number of elements: '))

for i in range(0, num):
    ele = int(input())
    array.append(ele)

print(array)


def insertion_sort(array):
    for i in range(1, len(array)):
        for j in reversed(range(0, i)):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


result = insertion_sort(array)

print("Result: ", result)
