n=int(input("Enter the number:"))
b=[]
for i in range(0,n):
  a=int(input("Element: "))
  b.append(a)
sum3=0
for j in b:
  if(j>0):
    print()
  else:
    sum3=sum3+j
print("Sum of all negative numbers:",sum3)
