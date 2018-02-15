a=int(input("Enter number: "))
k=0
if a==0:
    print("print valid number")
else:
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
    if(k<=0):
        print("Number is prime")
    else:
        print("Number isn't prime")
