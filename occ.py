def oneCount(n):
    n = str(n)
    if n == '1':
        return 1
    else:
        return 1 + oneCount(n[:-1])
m=raw_input("enter the digits: ")
print oneCount(m)
