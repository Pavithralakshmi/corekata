y=0
while y==0:
  n=int(input("enter your limits"))
  r=[]
  for i in range(1,n+1):
      a=input("enter a number")
      r.append(a)
  for i in range(1,n+1):
      print(max(r))
     r.remove(max(r))
  y=int(input("press 0 to continue"))
