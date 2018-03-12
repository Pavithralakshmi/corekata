def kk(m):
	n = len(m)
	rr = 1
	dd = 1
	qq = 1
	for i in range(0,n):
		if m[i] > 0:
			rr = rr*m[i]
			dd = min (dd * m[i], 1)
		elif m[i] == 0:
			rr = 1
			dd = 1
		else:
			temp = rr
			rr = max (dd * m[i], 1)
			dd = temp * m[i]
		if (qq < rr):
			qq = rr
	return qq
m = [9, -5, 4, -1, 3, 6,-8]
print "Maximum product subarray is",kk(m)


