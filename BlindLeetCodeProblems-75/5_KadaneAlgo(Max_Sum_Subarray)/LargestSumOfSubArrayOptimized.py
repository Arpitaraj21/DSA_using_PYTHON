def kadane(arr):
    current_sum = 0
    max_sum = float("-inf")
    
    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        
        if current_sum < 0:
            current_sum = 0
    
    return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]

print(kadane(arr))