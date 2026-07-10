# if we are not stopped from diving then

# what we will do is - we will multiply all the elements and then divide the product by each element
# we will get the product like that


nums = [1,2,3,4]


# matlab agar humko value chahiye toh index itself count nahi hoga uska left and right ke liye hum prefix and suffix array type kuch bana lenge


def productExceptSelf(arr):
    n = len(nums)
    answer = [1] * n
    
    # store left products
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
        
    
    suffix = 1
    for i in range(n-1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
        
    return answer

print(productExceptSelf(nums))