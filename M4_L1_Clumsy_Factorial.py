def clumsy_factorial(num):
    if num <= 2:
        return n

    stack = [num]
    num -= 1
    operations = ['*', '//', '+', '-']
    op_index = 0

    while num  > 0:
        if operations[op_index] == '*':
            stack[-1] *= num
        elif operations[op_index] == '//':
            stack[-1] //= num
        elif operations[op_index] == '+':
            stack.append(num)
        else:
            stack.append(-num)

        num -= 1
        op_index = (op_index + 1) % 4

    return sum(stack)
    

number = int(input().strip())

print(clumsy_factorial(number))
                                                                                                                            