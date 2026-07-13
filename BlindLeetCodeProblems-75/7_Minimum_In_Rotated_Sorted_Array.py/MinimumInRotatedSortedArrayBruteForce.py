arr = [4,5,6,7,0,1,2,3]

def MinimumInRotatedSortedArray(arr):
    min_value = float('inf')
    n = len(arr)
    for i in range(n):
        if arr[i] < min_value:
            min_value = arr[i]
    
    return min_value

print(MinimumInRotatedSortedArray(arr=arr))