print("cheack the given input is mulitiple by 7");
y=0
while y==0:
  num=int(input("enter ur first input"))
  if num>1:
    for i in range(1,num):  
      if num%7==0:
        print (num,"this number is multiple by 7")
        break
      else:
        print(num,"this number is  not multiple by 7")
      y=int(input("ënter 0 to continue else press 1"))
