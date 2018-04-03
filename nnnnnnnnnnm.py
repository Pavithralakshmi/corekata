print("nm")
y=0
while y==0:
  arr = str(input("enter somthing"))

  arr = list(map(lambda x: ord(x) - ord('a') + 1,arr))

  print(arr)
  y=int(input("press 0 to continue"))
  
