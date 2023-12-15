def manipulator(n, q, queries):
    array = [0] * n

    for query in queries:
        start, end, value = query
        array[start - 1] += value
        if end < n:
            array[end] -= value

    max_value = array[0]
    current_value = array[0]

    for i in range(1, n):
        current_value += array[i]
        max_value = max(max_value, current_value)

    return max_value


num = int(input().strip())
que = int(input().strip())

queries = []
for _ in range(que):
    query = list(map(int, input().strip().split()))
    queries.append(query)
print(manipulator(num, que, queries))