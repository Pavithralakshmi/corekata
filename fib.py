x=int(input("enter the limits:"))
f11=0
f21=1
print(f11)
print(f21)
for i in range(n-1):
    f3=f11+f21
    print(f3)
    f11=f21
    f21=f3
