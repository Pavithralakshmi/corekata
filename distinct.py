def hk(r, n, k):
	count = 0
	for i in range(0, n):
		for j in range(i+1, n) :
			if r[i] - r[j] == k or r[j] - r[i] == k:
				count += 1
	return count
r = [5, 4, 3, 2, 1, 5]
n = len(r)
k = 3
print ("Count of pairs with given diff is ",hk(r, n, k))
