def fibonacciMemo(n, memo={}):
    if memo.get(n):
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacciMemo(n - 1, memo) + fibonacciMemo(n - 2, memo)
    return memo[n]


def fibonacciTable(n):
    if n <= 2:
        return 1
    fib = [0, 1, 1]
    for i in range(3, n + 1):
        fib.insert(i,fib[i - 1] + fib[i - 2])
    return fib[n]


resultMemo = fibonacciMemo(20)
print("ResultMemo: ", resultMemo)

resultTable = fibonacciTable(10000)
print("ResultTable: ", resultTable)
