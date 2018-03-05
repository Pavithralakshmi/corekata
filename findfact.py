Num=int(input(&quot;Enter
a number: &quot;))

fac = 1
if num &lt; 0:
print(&quot;Sorry, factorial does not exist for negative numbers&quot;)
elif num == 0:
print(&quot;The factorial of 0 is 1&quot;)
else:
for i in range(1,num + 1):
fac = fac*i
print(&quot;The factorial of&quot;,num,&quot;is&quot;,fac)
