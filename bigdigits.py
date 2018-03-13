def pp(inum):
	count = [0 for x in range(10)]
	f = str(num)
	for i in range(len(f)):
		count[int(f[i])] = count[int(f[i])] + 1
	result = 0
	t = 1
	for i in range(10):
		while count[i] > 0:
			result = result + ( i * t )
			count[i] = count[i] - 1
			t = t * 10
	return result
num = 5657567567
print pp(num)
