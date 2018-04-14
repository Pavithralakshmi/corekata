def small():
	a=input("Enter the number:")
	b=int(input("Enter the digit to remove:"))
	l=[]
	for i in a:
		l.append(i)
	l.sort()
	s=''
	g=len(l)-b
	for i in range(g):
		s=s+l[i]
	print(int(s))
try:
	small()
except:
	print('invalid')
