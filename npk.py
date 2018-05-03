
n=int(input("enter n"))
s=str(n)
k=int(input("enter k"))
p=int(input("enter p"))
for i in range(len(s)):
  if (i+1==p):
    print(s[i+k])
    break
