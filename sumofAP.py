print(" operations")
def sumOfAP( a, d,n) :
    sum = 0
    i = 0
    while i < n :
        sum = sum + a
        a = a + d
        i = i + 1
    return sum
n = int(input("enter n value:"))
a = int(input("enter a value:"))
d = int(input("enter d value:"))
print ("sum of AP is: ",sumOfAP(a, d, n))
