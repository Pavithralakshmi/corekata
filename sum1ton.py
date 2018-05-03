def firstDigit(n) :
  while n >= 10: 
    n = n / 10;
  return int(n)
def lastDigit(n) :
  return (n % 10)
n = int(input("enter numbers"))
print(firstDigit(n), end = " ") 
print(lastDigit(n))
c=firstDigit(n)+lastDigit(n)
print(c)
