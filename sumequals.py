n=int(input("enter a num1"))
x=int(input("enter a num2"))
l=[]
for i in range(n):
  a=int(input())
  l.append(a)
if l[0]+l[1]==x:
  print("yes")
else:
  print("no")
