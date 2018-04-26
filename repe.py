s=256
c=[0]*s
m=-1
cc=''
a=input("enter anyrthing")
for i in a:
  c[ord(i)]+=1
  for i in a:
    if m<c[ord(i)]:
      m=c[ord(i)]
      cc=i
print(cc)    
