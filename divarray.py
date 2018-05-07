n=int(input("enter"))
a=[]
for i in range(n):
  b=int(input("enter element"))
  a.append(b)
print(a)
c=min(a)
for i in range(len(a)):
  d=a[i]//c
print(d)
