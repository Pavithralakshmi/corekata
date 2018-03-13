def uk(r, low, high, n):
	mid = low + (high - low)/2
	mid = int(mid)
	if ((mid == 0 or r[mid - 1] <= r[mid]) and
	(mid == n - 1 or r[mid + 1] <= r[mid])):
		return mid
	elif (mid > 0 and r[mid - 1] > r[mid]):
		return uk(r, low, (mid - 1), n)
	else:
		return uk(r, (mid + 1), high, n)
def Peak(r, n):
	return uk(r, 0, n - 1, n)
r = [1, 3, 20, 4, 1, 0]
n = len(r)
print("Index of a peak point is", Peak(r, n))
	
