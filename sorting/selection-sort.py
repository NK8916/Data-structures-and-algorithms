array = []

num = int(input('Enter the number of elements: '))

for i in range(0, num):
    ele = int(input())
    array.append(ele)

print(array)


def selection_sort(array):
    for i in range(0, len(array)):
        min = i
        for j in range(i, len(array)):
            if array[min] > array[j]:
                min = j
        if i != min:
            array[min], array[i] = array[i], array[min]
    return array


result = selection_sort(array)

print("Result: ", result)
