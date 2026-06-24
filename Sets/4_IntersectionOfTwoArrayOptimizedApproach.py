arr1 = [1, 2, 2, 3, 1]
arr2 = [2, 2,3]

def intersection(arr1,arr2):
    seen = set(arr1)
    result = set()
    
    for num in arr2:
        if num in seen:
            result.add(num)
        
    return list(result)
    

print(intersection(arr1=arr1, arr2=arr2))