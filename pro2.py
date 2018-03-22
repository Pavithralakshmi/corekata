def printArray(u, n):
    for i in range(0,n):
        print ("%d"%( u[i]),end=" ")
u = [23, 610, 270, 11, 12, 6, 7]
n = len(u)
pancakeSort(u, n);
print ("Sorted Array ")
printArray(u,n)
