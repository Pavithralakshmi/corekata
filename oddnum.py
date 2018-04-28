a=0
b=0
c=0
n=int(input("enter the n"))
m=int(input("enter the m"))
for i in range(n):
  a=int(input("enter ur element"))
  if a%2!=0:
    b=b+1
    if b==m:
      c=a
print(c)
