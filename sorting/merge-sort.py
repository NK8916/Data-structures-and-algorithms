array = []


num = int(input('Enter the number of elements: '))

for i in range(0, num):
    ele = int(input())
    array.append(ele)

print(array)


def mergesort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    return merge(mergesort(array[:mid]), mergesort(array[mid:]))


def merge(left, right):
    finalarray = []
    first = 0
    second = 0
    while first < len(left) and second < len(right):
        if left[first] < right[second]:
            finalarray.append(left[first])
            first += 1

        else:
            finalarray.append(right[second])
            second += 1

    while first < len(left):
        finalarray.append(left[first])
        first += 1

    while second < len(right):
        finalarray.append(right[second])
        second += 1

    return finalarray


result = mergesort(array)
print("Result: ", result)
