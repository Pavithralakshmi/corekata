print("cheack the given input is mulitiple by 7");
y=0
while y==0:
  first=int(input("enter ur first input"))
  second=int(input("enter ur secon input"))
  if first>1 and second>1:
    diff=first-second
    if diff==0:
      print (diff,"this id even")
      break
    elif diff%2==0:
      print(diff,"this is even")
      break
    else:
      print(diff,"this is odd")
    y=int(input("ënter 0 to continue else press 1"))
