a=[]
n=int(input("value"))
for i in range(1,n+1):
  b=int(input("numbers"))
  a.append(b)
  a.sort()
print(a)
print(a[n//2])
