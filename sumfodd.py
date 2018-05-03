
a=int(input("enter a"))
b=int(input("enter b"))
c=0
for i in range(a,b+1):
  if i%2!=0:
    c=c+i
print(c)
