year=int(raw_input("enter year to be cheak"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("this is leap yr",year)
else:
    print("not leap",year)
