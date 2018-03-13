def gt(s1, s2, m, n):
	if m == 0: return True
	if n == 0: return False
	if s1[m-1] == s2[n-1]:
		return gt(s1, s2, m-1, n-1)
	return gt(s1, s2, m, n-1)
s1 = "fdhfyufru"
s2 = "jfhfuhhjgk"
m = len(s1)
n = len(s2)
if gt(s1, s2, m, n):
	print "Yes"
else:
	print "No"
