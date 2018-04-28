a=0
b=0
l=[]
n=int(input("enter the n"))
m=int(input("enter the m"))
for i in range(n):
    a=int(input("enter ur element"))
    l.append(a)
for i in range(m-1):
    b=min(l)
    l.remove(b)
print(min(l))
