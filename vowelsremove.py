s=['a','e','i','o','u']
s1=input("enter the string")
l=[]
for i in range(len(s1)):
    if s1[i] not in s:
      l.append(s1[i])
a=l[::-1]
print(str(a))
