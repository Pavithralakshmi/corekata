print("***** LCM ******")
def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
         lcm = greater
         break
       greater += 1
   return lcm
s1 = int(input("enter first value"))
s2 = int(input("enter second value"))
print("The L.C.M. of", s1,"and", s2,"is", lcm(s1, s2))
