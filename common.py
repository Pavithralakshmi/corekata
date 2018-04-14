num=int(input("enter ur list length:"))
print(num)
c=list()
import os
for i in range(0,num):
  b=str(input("enter something:"))
  c.append(str(b))
print(c)
d=os.path.commonprefix(c)
print(d)
