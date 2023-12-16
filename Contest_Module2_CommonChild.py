def commonChild(string1, string2):
    len_string1 = len(string1)
    len_string2= len(string2)
    dp = [[0] * (len_string2 + 1) for _ in range(len_string1 + 1)]
    for i in range(1, len_string1 + 1):
        for j in range(1, len_string2 + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len_string1][len_string2]
in_string1 = str(input())
in_string2 = str(input())
print(commonChild(in_string1, in_string2))