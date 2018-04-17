def gcd(x,y):
  while(y):
    x,y=y,x%y
  return x
x=int(input()) 
y=int(input())
if(gcd(x,y)==1):
  print("Relatively prime")
else:
  print("Not relatively prime")
