# Brute Force Approach
#  return the results that are Intersecting
arr1 = [1, 2, 2, 1]
arr2 = [2, 2]

def intersection(arr1, arr2):
    result = []
    
    for i in arr1:
        for j in arr2:
            if i == j and i not in result:
                result.append(i)
            
    return result

print(intersection(arr1, arr2))