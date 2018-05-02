a=input("enter string")
b=input("enter string")
c=1
for i in a: 
  if i in b:
    c=0
    break
if(c==0):
  print("yes")
else:
  print("no")
