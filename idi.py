from numpy import *
x = range(int(input("x")))
x = reshape(x,(4,4))
print(x) 
n = int(input("enter row limits"))
m = int(input("enter col limits"))
a = [0] * n
for i in range(n):
    a[i] = [0] * m
    print("  ")
print(a)
