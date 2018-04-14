print("print str with omit first letter")
y=0
while y==0:
  s1=str(input("Enter first string:"))
  s2=str(input("Enter second string:"))
  if(sorted(s1)==sorted(s2)):
        print("The strings are anagrams.")
  else:
        print("The strings aren't anagrams.")
  y=int(input("press 0 to continue"))
  
