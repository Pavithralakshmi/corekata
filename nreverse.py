n=int(input(&quot;EnterThe Number:&quot;))
rev=0
while(n&gt;0):
  dig=n%10
  rev=rev*10+dig
  n=n//10
  print(&quot;Reverseof the number:&quot;,rev)
