y=0
while y==0:
  def prg(l,n):
  	cc=0
  	for i in range(n):
  		for j in range(n):
  			if l[i]==l[j]:
  				cc=cc+1
  		if cc==1:
  			print(l[i])
  		cc=0
  def main():
  	n=int(input("enter ur limits"))
  	l=[]
  	for i in range(n):
  		l.append(int(input("enter ur elements")))
  	prg(l,n)
  try:
  	main()
  except:
  	print('invalid')
  y=int(input(" press 0 to continue"))
  	
