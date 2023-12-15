def sliding_beauty(arr, k, n):
    out = []
    for i in range(len(arr) - k + 1):
        subarray = arr[i:i + k]
        sorted_subarray = sorted(subarray)
        out.append(sorted_subarray[n - 1])
    return out


arr = list(map(int, input().strip().split()))
k = int(input().strip())
n = int(input().strip())


out = sliding_beauty(arr, k, n)
print(*out)