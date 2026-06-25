arr = [1,2,5 ,3,4]

n = len(arr)

for i in range(n):
    swapped = True
    
    for j in range(0, n - i -1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        
    if not swapped:
        break
    
print(arr)