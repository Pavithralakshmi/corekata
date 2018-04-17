def large( a, n):
    for i in range(n):
        if a[abs(a[i])-1] > 0:
            a[abs(a[i])-1] = -a[abs(a[i])-1]
        else:
            print("repeating number",abs(a[i]))
             
    for i in range(n):
        if a[i]>0:
            print(" missing number ",i+1)
a = [6, 2,46, 3, 44, 6, 5, 2]
n = len(a)
print(large(a,n))
