def max_chunks(arr):
    n = len(arr)
    max_value = 0
    chunks = 0
    for i in range(n):
        max_value = max(max_value, arr[i])
        if max_value == i:
            chunks += 1
    return chunks
input_arr =input().split(" ")
processed_arr=[int(ch) for ch in input_arr]
print(max_chunks(processed_arr))