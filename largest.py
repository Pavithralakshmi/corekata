a=int(raw_input("enter your choices"))
b=int(raw_input("enter your choices"))
c=int(raw_input("enter your choices"))
if a>b&a>c:
    print("a is greatest",a)
elif b>c:
    print("b greatest",b)
elif a<c:
    print("c is greatest",c)
elif a==b==c:
    print("all are equal",a,b,c)
else:
    print("print valid number")
