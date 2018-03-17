print("*****palindrom yes or no ******")
y=0
while y==0:
  s=input("enter input")
  s=s.casefold()
  rev=reversed(s)
  if list(s)==list(rev):
    print(" yes it is palindrom")
  else:
    print(" no it is not palindrom")
  y=int(input("select 1 to exit else 0 to continue"))
