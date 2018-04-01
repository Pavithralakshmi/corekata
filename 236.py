print("check the given input is in between string")
y=0
while y==0:
  l=int(input("enter your strating limit"))
  h=int(input("enter your ending limit"))
  n=int(input("enter your input:"))
  if n>l & n<h:
    print(n,"yes,this is in between value")
  else:
    print(n," no, this is not in between")
  y=int(input("press 0 to continue"))
