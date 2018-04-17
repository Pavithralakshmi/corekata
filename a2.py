def max( a, size):
    for i in range(size):
        if a[abs(a[i])-1] > 0:
            a[abs(a[i])-1] = -a[abs(a[i])-1]
        else:
            print("repeating number",abs(a[i]))
             
    for i in range(size):
        if a[i]>0:
            print(" missing number ",i+1)
a = [6, 2, 3, 4, 4, 5, 2]
n = len(a)
printmax(a,n)
