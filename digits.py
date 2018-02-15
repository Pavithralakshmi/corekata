n=int(raw_input("enter the number of values"))
if n>0:
    count=0
    while n>0:
        count=count+1
        n=n//10
    print(count)
else:
    print("invalid")
