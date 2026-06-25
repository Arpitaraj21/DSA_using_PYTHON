arr = [10,20,30,40,50]
target = 20

def BinarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            mid = mid + 1
        
        else:
            mid = mid - 1
            
            
            
print(BinarySearch(arr, target=30))