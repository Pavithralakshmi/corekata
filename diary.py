print("diary notes")
y=0
while y==0:
  n=int(input("Enter the N value:"))
  print("Enter the Elements:")
  a=[0]
  sum=0
  for x in range(n):
  	k=int(input())
  	a.append(k)
  for x in range(n):
  	sum=sum+a[x]
  print(sum)
  y=int(input("press 0 to continue"))
