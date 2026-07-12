def ProductArrayExceptSelf(array):
    n = len(array)
    prefix = [1] * n
    suffix = [1] * n
    ans = [1] * n

    for i in range(1, n):
        prefix[i] = prefix[i-1] * array[i-1]
    
    for i in range(n-2,-1,-1):
        suffix[i] = suffix[i+1] * array[i+1]

    for i in range(n):
        ans[i] = prefix[i] * suffix[i]

    return ans

array = [1,2,3,4]
print(ProductArrayExceptSelf(array=array))