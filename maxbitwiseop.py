def or(arr,n):
  ans = -2147483648
  for i in range(n):
    c = 0
    for j in range(i,n):
      c = c | arr[j]
      ans = max(ans, c)
  return ans
arr = [8, 1, 2, 12]
n = len(arr)
 
print("Max subarray OR is ",or(arr, n))
