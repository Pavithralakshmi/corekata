print("product")
y=0
while y==0:
  def countDigits(a) :
    count = 0
    while (a > 0) :
      count = count + 1
      a = a // 10
    return count
  a = int(input("enter first value"))
  print("Number of digits = ",countDigits(a))
  y=int(input("press 0 to continue"))
      
