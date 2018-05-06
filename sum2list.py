import numpy as np
l=[]
m=[]
n=int(input("enter:"))
for i in range(n):
  a=int(input("enter"))
  l.append(a)
for i in range(n):
  b=int(input("enter"))
  m.append(b)
y=np.array(l)
yy=np.array(m)
g=y+yy
print(l)
print(m)
print(g)
