n=int(input("enter limits"))
s=[]
for i in range(n):
  a=int(input("enter ur elements"))
  s.append(a)
for j in range(n):
  if j==n-1:
    break
  if s[j]+1==s[j+1]:
    pass
  else:
    print(s[j+1])
    break
