aa=input('')
b=0
for i in aa:
  if int(i)%2!=0:
    b=b+int(i)
print(b)
if b%2==0:
  print('E')
else:
  print("O")
