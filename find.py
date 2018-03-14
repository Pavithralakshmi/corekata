l = [11, 65, 2, 3, 1, 2, 4, 5]

r = int(input("Enter number to search: "))

found = False

for i in range(len(l)):
 if(l[i] == r):
  found = True
  print("%d found at %dth position"%(r,i))
  break
 
if(found == False):
 print("%d is not in list"%r)
