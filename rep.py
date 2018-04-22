n=int(input("enter ur limits"))
l1=[]
l2=[]
b=0
for i in range(n):
  a=int(input("enetr your elements"))
  l1.append(a)
for i in range(n):
  b=l1.count(l1[i])
  if b==2:
    l2.append(l1[i])
    break
l2.sort()
s=set(l2)
if len(s)!=0:
  print(s)
  print(len(s))
else:
  print("unique")
