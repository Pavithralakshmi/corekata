def prg(n1,n2):
	while(n2!=0):
		t=n2
		n2=n1%n2
		n1=t
	return n1
def main():
	m=int(input())
	q=int(input())
	(l,r)=([],[])
	for i in range(m):
		l.append(int(input()))
	print(l)
	for c in range(q):
		n1=int(input())
		n2=int(input())
		r.append(prg(l[n1-1],l[n2-1]))
	for i in r:
		print(r)
try:
  main()
except:
  print('invalid')
