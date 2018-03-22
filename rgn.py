def sum_digits(n):
    ss = 0
    while n:
        ss += n % 10
        n //= 10
    return ss
