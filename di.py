a=int(input("enter some"))
b=""
while(a!=0):
  b=b+' '+str(a%10)
  a=a//10
print(b[::-1])
