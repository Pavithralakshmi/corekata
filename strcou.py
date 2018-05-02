a=input("enter string")
b=input("enter word")
c=a.split(" ")
count=0
for i in range(0,len(c)):
  if b==c[i]:
    count+=1
print(count)
