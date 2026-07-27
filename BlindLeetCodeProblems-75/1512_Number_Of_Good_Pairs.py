nums = [1,1,1,1]

def NumberOfGoodPairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] == nums[j] and i < j:
                count += 1
        
    return count

print(NumberOfGoodPairs(nums=nums))