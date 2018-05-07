def li(a, n, num1, num2):
  for i in range(0,n):
    if (a[i] == num1):
      break
    if (i >= n-1):
      return 0
    for j in range(n-1, i+1, -1):
      if (a[j] == num2):
        break
      if (j == i):
        return 0
    return (j - i - 1)
a= [ ]
n=int(input("enter limit"))
num1 = int(input("enter "))
num2 = int(input("enter "))
for i in range(n):
  b=int(input("enter element"))
  a.append(b)
print(li(a, n, num1, num2))
 
