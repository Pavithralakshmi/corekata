n=int(input("enter a num1"))
l1=[]
l=[]
for i in range(n):
  a=int(input())
  l.append(a)
for i in range(n):
  b=int(input())
  l1.append(b)
s=set(l)
s1=set(l1)
print(s&s1)
