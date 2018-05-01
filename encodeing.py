s=input("enter")
for i in s:
	if ord(i)>=120 or ord(i)==121 or ord(i)==122:
		b=chr(96+3-(122-ord(i)))
	elif ord(i)==88 or ord(i)==89 or ord(i)==90:
		b=chr(64+3-(90-ord(i)))
	else:
		b= chr(ord(i) + 3)
	print(b,end="")
	
