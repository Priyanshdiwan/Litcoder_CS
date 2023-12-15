def egyptian_mathematician(num, deno):
    result = []

    while num != 0:
        unit_fraction_denominator = -(-deno // num)
        result.append(unit_fraction_denominator)

        num = num * unit_fraction_denominator - deno
        deno = deno * unit_fraction_denominator

    return result

numerator = int(input().strip())
denominator = int(input().strip())

result = egyptian_mathematician(numerator, denominator)
for fraction in result:
    print(fraction)