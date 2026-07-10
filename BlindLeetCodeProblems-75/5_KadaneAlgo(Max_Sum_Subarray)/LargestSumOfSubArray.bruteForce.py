nums = [2, 3, 5, -2, 7, -4]

def LargestSum(nums):
    max_sum = float('-inf')
    n = len(nums)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
    print([i, j])
    return max_sum


print(LargestSum(nums=nums))