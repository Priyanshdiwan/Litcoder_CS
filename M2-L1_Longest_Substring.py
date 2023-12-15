def longeststring(string):
    n = len(string)
    if n<2:
        return n
    left=0
    char_set=set()
    result=0
    
    for right in range(n):
        while string[right] in char_set:
            char_set.remove(string[left])
            left +=1
            
        char_set.add(string[right])
        result = max(result, right - left +1)
    return result 
string_in= input()
out= longeststring(string_in)
print(f"{out}")