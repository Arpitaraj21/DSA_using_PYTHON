arr = [1,2,3,3,4,2,4,5,1,4]

def CountDistinctElement(arr):
    seen = set()
    for num in arr:
        seen.add(num)
        
    return len(seen)

print(CountDistinctElement(arr))