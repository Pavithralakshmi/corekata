a=input("enter the string")
b=len(a)//2
print(b)
for i in range(len(a)):
  if i==b:
    print(a[i])
    s=a.replace(a[i],'*')
print(s)
