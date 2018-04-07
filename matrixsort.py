x=[]
print(" totalno of elements",end='')
n=int(input(" enter no :"))
for i in range(n):
  print('enter element:',end='')
  x.append(int(input()))
print('original list',x)
flag=False
for i in range(n-1):
  for j in range(n-1-i):
    if x[j]>x[j+1]:
      t=x[j]
      x[j]=x[j+1]
      x[j+1]=t
      flag=True
if flag==False:
  print("")
else:
  flag=False
print("ssorted list:",x)
