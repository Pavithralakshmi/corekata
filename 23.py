a=input("enter a string")
b=1
for i in range(len(a)):
  if i==0 or i==1:
    b=0
  else:
    b=1
    break
if b==0:
    print("binary")
else:
    print("not a binary")
 
