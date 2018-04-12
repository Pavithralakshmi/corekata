def reg():
	f=1
	n1=int(input())
	for i in range(1,n1):
		f=f*i
	print(f)
try:
	reg()
except:
	print('invalid')
  
