from sets import Set
def conseq(p, n):
	s = Set()
	t=0
	for ele in p:
		s.add(ele)
	for i in range(n):
		if (p[i]-1) not in s:
			j=p[i]
			while(j in s):
				j+=1
			t=max(t, j-p[i])
	return t 
if __name__=='__main__':
	n = 7
	p = [1, 8, 6, 17, 4, 248, 2]
	print "Length of the Longest contiguous subsequence is ", 
	print conseq(p, n)
		
