a=int(input("enter a number"))
b=int(input("enter b number"))
if(a>b):
  if(b+b<a):
    print("no")
  else:
    print("yes")
elif(a<b):
  if(a+a<b):
    print("no")
  else:
    print("yes")
else:
    print("no")
