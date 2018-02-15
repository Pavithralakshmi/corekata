print("factorial")
f=1
n=int(raw_input("enter the value"))
if n<0:
    print("invalid")
elif n==0:
    print("value is 1")
else:
    for i in range(1,n+1):
        f=f*i
    print("the fact is",f)
