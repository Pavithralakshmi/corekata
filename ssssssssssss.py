str1=input("enter string1")
str2=input("enter string2")
c=0
for i in range(0,len(str1)):
    if(str1[i]!=str2[i]):
        c+=1
if(c==1):
    print("yes")
else:
    print("no")
           
