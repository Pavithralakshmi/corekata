def tri(n):
  num=1
  for i in range(0,n):
    for j in range(0,i+1):
      print(num,end="")
      num=num+1
    print("")
  a= num-1
  sum1 = 0
  while(a > 0):
    sum1=sum1+a
    a=a-1
  print("The sum of first n natural numbers is",sum1)
n=int(input("enter no of row"))
tri(n)
