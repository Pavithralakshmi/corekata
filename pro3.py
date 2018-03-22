def sum_digits(n):
    sss = 0
    while n:
        sss += n % 10
        n //= 10
    return sss
