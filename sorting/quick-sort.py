array = []


num = int(input('Enter the number of elements: '))

for i in range(0, num):
    ele = int(input())
    array.append(ele)

print(array)

start = 0
end = len(array)


def pivot(array, start, end):
    pivotItem = array[start]
    pivotindex = start

    for i in range(start, end):
        print("array: ", array, "pivotIndex: ", pivotindex)
        if pivotItem > array[i]:
            pivotindex += 1
            array[pivotindex], array[i] = array[i], array[pivotindex]

    array[start], array[pivotindex] = array[pivotindex], array[start]
    print("after: ", array)

    return pivotindex


def quickSort(array, left, right):
    if left < right:
        pivotIndex = pivot(array, left, right)
        quickSort(array, left, pivotIndex)
        quickSort(array, pivotIndex + 1, right)
    return array


result = quickSort(array, 0, len(array))

print("Result: ", result)
