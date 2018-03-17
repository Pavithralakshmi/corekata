print("*****math operations******")
s1=int(input("enter uour number"))
s2=int(input("enter your number"))
y=0
while y==0:
  ch=int(input("enetr youroptions"))
  if ch==1:
    print("    addition   ")
    print("the value is",s1+s2)
  elif ch==2:
    print("    subtration   ")
    print("the value is",s1-s2)
  elif ch==3:
    print("    multiplication   ")
    print("the value is",s1*s2)
  elif ch==4:
    print("    division   ")
    print("the value is",s1/s2)
  elif ch==5:
    print("    reminder   ")
    print("the value is",s1%s2)
  else:
    print("invalid")
  y=int(input("enter 0 to continue 1 to exist" ))
