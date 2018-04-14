print("count string albha order")
y=0
while y==0:
  a=list(str(input("enter something")))
  b=list(str(input("enter somthing")))
  x=len(a)
  c=0
  i=0
  j=0
  while x>0:
    c=c+(ord(b[j])-ord(a[i]))
    i=i+1
    j=j+1
    x=x-1
  print(c)
  y=int(input("press 0 to continue"))
