print("remove repeating charter")
n=input("enter string")
a=[]
b=""
for i in range(len(n)):
    a.append(n[i])
s=set(a)
b=', '.join(n)
print(b)
