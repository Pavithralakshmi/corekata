import collections
n=int(input("enter your limkits"))
a=[]
for i in range(n):
    b=int(input())
    a.append(b)
c = collections.Counter(a)
print(min(c))
