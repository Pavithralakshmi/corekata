a=int(input("enter number"))
b=0
for i in range(2,a):
  if(a%i==0):
    print("yes")
    b=1
    break
if b==0:
    print("no")
