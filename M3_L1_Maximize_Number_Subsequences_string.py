def count_max( text: str, pattern: str) -> int:
    count0 = count1 = countPattern = 0
    for c in text:
        if c == pattern[1]:
            count1 += 1
            countPattern += count0
        if c == pattern[0]:
            count0 += 1
    
    return countPattern + max(count1, count0)


text = input().strip()
pattern = input().strip()
print(count_max(text, pattern))