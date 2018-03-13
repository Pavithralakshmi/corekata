def pp(r):
	left,right = 0,len(r)-1
	while left < right:
		while (r[left]%2==0 and left < right):
			left += 1
		while (r[right]%2 == 1 and left < right):
			right -= 1
		if (left < right):
			r[left],r[right] = r[right],r[left]
			left += 1
			right = right-1
r = [17, 34, 74, 99, 8, 90, 53]
pp(r)
print ("Array after segregation "),
for i in range(0,len(r)):print r[i],
