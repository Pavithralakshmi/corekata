def rr(l,s,e,ss):
	sum=0
	for i in range(s,e+1):
		if l[i]==l[ss+1] or l[i]==l[ss-1]:
			continue
		sum+=l[i]
	return sum
def r(l,s,e):
	sum=0
	for i in range(s,e+1):
		sum+=l[i]
	return sum
def main():
	n=int(input())
	l=[]
	max=-1
	for i in range(n):
		l.append(int(input()))
	for i in range(n):
		if i==0:
			s=r(l,i+2,n-1)
		elif i==n-1:
			s=r(l,0,n-3)
		else:
			s=rr(l,0,n-1,i)
		if max<s:
			max=s
	print(max)
try:
  main()
except:
  print('invalid')
