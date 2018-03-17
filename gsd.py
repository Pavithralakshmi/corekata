print("***** GSD ******")
def computeHCF(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
s1 = int(input("enter first value"))
s2 = int(input("enter second value"))
print("The H.C.F. of", s1,"and", s2,"is",computeHCF(s1, s2))
