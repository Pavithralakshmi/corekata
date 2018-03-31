print("check the input is between the range")
y=0
while y==0:
  num=int(input("enter your value"))
  for i in range(1):
    if num<10:
      print(num," yes,this range is in between 1 to 10 ")
    else:
      print( num," no,this is not in range")
  y=int(input("0 to continue"))
