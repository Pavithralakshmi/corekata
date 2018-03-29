print("cheack the input is prime or not");
y=0
while y==0:
  num=int(input("enter ur first input"))
  if num>1:
    for i in range(2,num):  
      if num%i==0:
        print ("this is prime number",num)
        break
      else:
        print("this is not a prime a number",num)
  y=int(input("ënter 0 to continue else press 1"))
