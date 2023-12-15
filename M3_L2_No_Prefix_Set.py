def good_or_bad(passwords):
    passwords.sort()
    for i in range(len(passwords) - 1):
        if passwords[i + 1].startswith(passwords[i]):
            return "BAD PASSWORD"
    return "GOOD PASSWORD"
passwords = input().strip().split()

result = good_or_bad(passwords)
print(result)