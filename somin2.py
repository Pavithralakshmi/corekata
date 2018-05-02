a=int(input("enter number a:"))
b=int(input("enter number b:"))
l=[]
for i in range(a):
  c=int(input("enter number c:"))
  l.append(c)
for i in range(b-1):
  c=min(l)
print(min(l))
