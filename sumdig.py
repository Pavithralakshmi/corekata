n=int(input("enter num"))
b=0
while(n!=0):
   a=n%10
   b=b+(a*a)
   n=n//10
print(b)
