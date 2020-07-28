import math
from itertools import chain

array = []

num = int(input('Enter the number of elements: '))

for i in range(0, num):
    ele = int(input())
    array.append(ele)

print(array)


def mostDigits(array):
    max_digit = 0
    for i in range(0, len(array)):
        max_digit = max(max_digit, digitcount(array[i]))
    return max_digit


def digitcount(num):
    count = len(list(str(num)))

    return count


def getDigit(num, place):
    divisor = math.pow(10, place)
    digit = int((num / divisor) % 10)

    return digit


def radixsort(array):
    maxdigit = int(mostDigits(array))
    for k in range(0, maxdigit):
        r, c = len(array), 10
        bucketarray = [[] for y in range(c)]
        for i in range(0, len(array)):
            digit = getDigit(array[i], k)
            bucketarray[digit].append(array[i])
        array = list(chain.from_iterable(bucketarray))

    return array


result = radixsort(array)

print("Result: ", result)
