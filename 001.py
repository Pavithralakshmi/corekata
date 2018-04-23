n=int(input("enter ypur limits"))
l1=[]
l2=[]
for i in range(n):
    a=int(input())
    l1.append(a)
for i in range(n):
    if (i%2!=0 and l1[i]%2==0) or (i%2==0 and l1[i]%2!=0):
        l2.append(l1[i])
print(l2)
