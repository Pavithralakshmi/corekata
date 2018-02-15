num=int(input("Enter number:"))
temp=num
re=0
while(num>0):
    dig=n%10
    re=re*10+dig
    num=num//10
if(temp==re):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
