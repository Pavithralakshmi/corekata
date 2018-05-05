n=int(input("Enter the number:"))
b=[]
c=[]
for i in range(0,n):
  a=int(input("Element: "))
  b.append(a)
print(b)
for j in range(0,n):
  c=b[::-1]
print(c)
if(c==b):
  print("yes")
else:
  print("n0")
