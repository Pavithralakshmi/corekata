n = 2
a = [[1,342,4],[44,25,6]]
first = sum(a[i][i] for i in range(n))
second = sum(a[n-i-1][n-i-1] for i in range(n))
print(str(first)+" "+str(second))
      
