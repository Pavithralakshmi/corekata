def printArray(r, n):
    for i in range(0,n):
        print ("%d"%( r[i]),end=" ")
r = [243, 140, 240, 141, 142, 46, 74]
n = len(r)
pancakeSort(r, n);
print ("Sorted Array ")
printArray(r,n)
