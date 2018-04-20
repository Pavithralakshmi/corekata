n=int(input("enter your limits"))
n1=int(input("enter your limits"))
s=input("Enter two numbres to be checked in array:")
b=[]
c=[]
for i in range(1,n+1):
  a=input("enter a number")
  b.append(a)
for i in range(1,n1+1):
  d=input("enter d number")
  c.append(d)
if((s in a) and (s in d)):
  print("yes")
else:
  print("no")
y=int(input("press 0 to continue"))
  
