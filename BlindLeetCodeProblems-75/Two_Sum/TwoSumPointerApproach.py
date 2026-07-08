arr = [2,6,5,8,11]
target = 14  

def twoSum(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1

    while(left< right):
     if arr[left] + arr[right] == target:
        return "Yes"
     elif arr[left] + arr[right] > target:
        right -= 1
     else:
        left += 1

print(twoSum(arr=arr, target=target))

