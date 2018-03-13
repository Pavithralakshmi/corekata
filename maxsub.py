from sys import maxint
def rd(a,size):
	j = -maxint - 1
	d = 0
	for i in range(0, size):
		d = d + a[i]
		if (j < d):
			j = d
		if d < 0:
			d = 0
	return j
a = [-18, -23, -5, -2, -23, -12, -2, -1, -54, -2, -1, -45, -17]
print "Maximum contiguous sum is", rd(a,len(a))
