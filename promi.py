r=int(input("Enter upper limit: "))
e=[]
u=0
for a in range(2,r+1):
  k=0
  for i in range(2,a//2+1):
    if(a%i==0):
      k=k+1
    if(k<=0):
      u=u+a
      e.append(a)
    if r==u:
      print(e)
