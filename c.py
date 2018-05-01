n=int(input("enter the number"))
b=1
for i in range(2,n):
  if n%i==0 and n!=2:
    b=0
if b==0:
  print("yes")
else:
  print("no")
 
