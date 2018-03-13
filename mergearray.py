def ttt(a, b, res, n, m):
	i, j, k = 0, 0, 0
	while (i < n):
		res[k] = a[i]
		i += 1
		k += 1
	while (j < m):
		res[k] = b[j]
		j += 1
		k += 1
	res.sort()
a = [ 70, 52, 5 ]
b = [ 70, 13, 32, 13 ]
n = len(a)
m = len(b)
res = [0 for i in range(n + m)]
ttt(a, b, res, n, m)
print "Sorted merged list :"
for i in range(n + m):
	print res[i],
