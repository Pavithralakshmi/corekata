l = []
y=[]
n=int(input("enter:"))
m=int(input("enter:"))
for i in range(1,n+1):
  b=int(input("enter"))
  l.append(b)
for j in range(1,m):
  c=int(input("enter"))
  y.append(c)
print(l)
print(y)
print( max(l) or max(y))
