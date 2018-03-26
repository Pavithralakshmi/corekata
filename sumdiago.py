n=int(input())
m=[[int(i) for i in input().split()]for j in range(n)]
s=sum(m[i][i] for i in range(n))
s1=sum(m[i][n-i-1] for i in range(n))
if n%2!=0:
    print(s+s1-m[n//2][n//2])
else:

    print(s+s1)
