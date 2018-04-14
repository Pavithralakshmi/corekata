s1=input("Enter s1 String:")
s2=input("Enter s2 String:")
a=list(s1)
b=list(s2)
c=[]
cost=0
l1=len(s1)
l2=len(s2)
if l1!=l2:
	for x in range(l2-l1):
		a.append(" ")
for x in range(max(l1,l2)):
	if a[x]!=b[x]:
		cost=cost+1
print("Ans:",cost)
