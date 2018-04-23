y=0
while y==0:
  n=int(input("enter ur limits"))
  m=int(input("enter ur limits"))
  r=[]
  b=0
  c=0
  for i in range(n):
      b=int(input("enter value"))
      r.append(b)
  print(r)
  for i in range(n):
      if i==n-1:
          break
      else:
          if r[i]+r[i+1]==m:
              c=0
              break
          else:
              c=1
  if c==0:
      print("yes")
  else:
      print("no")
  y=int(input("press 0 to continue"))
