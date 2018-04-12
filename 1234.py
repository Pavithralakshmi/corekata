num=int(input("enter total"))
l=[]
for i in range(0,num):
    a=int(input())
    l.append(a)
a=sorted(l,reverse=True)
b=list(map(int,a))
print(b)
