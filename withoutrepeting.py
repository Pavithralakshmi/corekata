CHARS = 256
def rr(string):
	n = len(string)
	cur = 1	 
	max= 1	 
	index = 0 
	i = 0
	visited = [-1] * CHARS
	visited[ord(string[0])] = 0
	for i in xrange(1,n):
		index = visited[ord(string[i])]
		if index == -1 or (i - cur > index):
			cur+=1
		else:
			if cur > max:
				max = cur
			cur = i - index
		visited[ord(string[i])] = i
	if cur > max:
		max = cur
	return max
string = "my name is billa"
print "The input string is " + string
length = rr(string)
print ("The length of the longest non-repeating character" +" substring is " + str(length))



