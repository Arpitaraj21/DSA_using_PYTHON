Nums = [1,2,-3,0,-4,-5]

def MaximumProduct(nums):
    max_product = float('-inf')
    n= len(nums)
    for i in range(n):
        current_product = 1
        for j in range(i, n):
            current_product *= nums[j]
            max_product = max(max_product, current_product)
            
    return max_product

print(MaximumProduct(nums=Nums))
        