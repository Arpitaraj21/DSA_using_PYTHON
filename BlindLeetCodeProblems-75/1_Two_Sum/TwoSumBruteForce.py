arr = [2,6,5,8,11]
target = 14  

def twoSum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
           if arr[i] + arr[j] == target:
             return "Yes"
        
    return "No"

print(twoSum(arr=arr, target=target))