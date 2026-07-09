arr = [1, 2, 3,1]

def ContainDuplicate(arr):
    arr.sort()
    for i in range(len(arr) -1):
        if arr[i] == arr[i+1]:
            return True
        
    return False 

print(ContainDuplicate(arr))