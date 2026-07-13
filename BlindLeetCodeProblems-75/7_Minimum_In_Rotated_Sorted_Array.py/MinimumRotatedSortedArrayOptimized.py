arr = [4,5,6,7,0,1,2,3]


def MinimumRotatedSortedArray(arr):
    left = 0
    right = len(arr) - 1
    
    min_value = float('inf')
    
    while left <= right:
        mid = left + (right - left) // 2
        
        
        if arr[left] <= arr[mid]:
            min_value = min(min_value, arr[left])
            left = mid + 1
        
        else:
            min_value = min(min_value, arr[mid])
            right = mid - 1
            
    return min_value

print(MinimumRotatedSortedArray(arr=arr))