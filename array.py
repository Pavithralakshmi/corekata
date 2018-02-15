n=int(raw_input("Enter number:"))
a=int(raw_input("enter sum value"))
ll=[]
s=0
for i in range(0,n):
    l=int(raw_input("enter values"))
    ll.append(l)
for i in range(0,a):
    s+=int(ll)
print(s)
