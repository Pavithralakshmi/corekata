a=int(input("enter a number"))
l=[]
for i in range(2,100):
  b=1
  for j in range(2,i):
    if(i%j==0):
      b=0
      break
    if(b==1):
      l.append(i)
for i in range(0,len(l)):
  if(a%l[i]==0):
    print(l[i])
