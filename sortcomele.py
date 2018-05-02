n=int(input("enter a num1"))
k=int(input("enter a num2"))
l=[]
for i in range(n):
  a=int(input())
  if a<k:
    l.append(a)
l.sort()
print(l)
