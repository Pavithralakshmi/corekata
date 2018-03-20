def ff(a,n):
    ss=0
    for i in range(0,n):
        ss+=a[i]
    return float(ss/n)
def findMedian(a,n):
    sorted(a)
    if n%2!=0:
        return float(a[n/2])
    return float((a[int((n-1)(2)]+a[int(n/2)])/2.0)
a=[1,34,4,2,7,5,68,6]
n=len(a)
print("meadian'",ff(a,n))
