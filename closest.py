def xxx(a,a_size):
    inv_count = 0
    if a_size < 2:
        print("Invalid Input")
        return
    min_l = 0
    min_r = 1
    min_sum = a[0] + a[1]
    for l in range (0, a_size - 1):
        for r in range (l + 1, a_size):
            sum = a[l] + a[r]                 
            if abs(min_sum) > abs(sum):         
                min_sum = sum
                min_l = l
                min_r = r
    print("The two elements whose sum is minimum are", 
            a[min_l], "and ", a[min_r])
a = [1, 67, -16, 7, -8, 8, 56]
 
xxx(a, 7);
 
