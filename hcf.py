def computeHCF(x, y):
  if x > y:
    smaller = y
  else:
    smaller = x
  for i in range(1, smaller+1):
    if((x % i == 0) and (y % i == 0)):
      hcf = i
  return hcf
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("",computeHCF(x, y))
