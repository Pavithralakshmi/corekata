n=int(input("enter ur limits"))
a=1
for i in range(2,n):
  if n%i==0:
    print(i)
    a=0
if a==0:
  print("yes")
else:
  print("no")
