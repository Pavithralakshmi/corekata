def lenarr(a, n) :
	m = 1
	l = 1
	for i in range(1, n) :
		if (a[i] > a[i-1]) :
			l =l + 1
		else :
			if (m < l) :
				m = l  
			l = 1
	if (m < l) :
		m = l
	return m
a = []
n=int(input("enter limit:"))
for i in range(n):
  b=int(input("enter element:"))
  a.append(b)
print("Length = ", lenarr(a, n))
