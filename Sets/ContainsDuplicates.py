arr = [1,2,3,4,2,4,3]

seen = set()

def ContainsDuplicates(arr): 
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
        
    return False

print(ContainsDuplicates(arr))
print(seen)