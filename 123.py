num=int(input())
sec=int(input())
li=[]
a=[]
for i in range(0,num):
	li.append(int(input()))
for i in range(0,sec):
	s=0
	u=int(input())
	v=int(input())
	maxi=li[u-1]		
	for j in range(u,v):
		if(maxi<li[j]):
				maxi=li[j]
	a.append(maxi)
print(a)
