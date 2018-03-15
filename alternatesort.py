def gh(r, n):
	r.sort() 
	i = 0
	j = n-1
	while (i < j): 
		print(r[j], end =" ")
		j-= 1
		print(r[i], end =" ")
		i+= 1
	if (n % 2 != 0):
		print(r[i]) 
r = [10, 102, 49, 86, 757, 105] 
n = len(r)
gh(r, n)
