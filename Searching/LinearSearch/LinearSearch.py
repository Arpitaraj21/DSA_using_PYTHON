arr = [10,20,30,40]
target = 40

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    return -1

print(linear_search(arr, target=40))




# using enumerate()
for index, value in enumerate(arr):
    if value == target:
        print(index)

