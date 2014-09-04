def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    if exponent & 1 == 0:
        result = power(base, exponent >> 1)
        result *= result
    else:
        result = power(base, exponent >> 1)
        result *= result
        result *= base
    return result


print power(2, 10)