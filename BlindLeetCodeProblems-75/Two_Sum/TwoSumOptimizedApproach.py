arr = [2,6,5,8,11]
target = 12


def twoSum(arr, target):
    seen = {}

    for i in range(len(arr)):
        need = target - arr[i]

        if need in seen:
            # return index
            return [seen[need], i]
            # return "Yes"
        
        
        seen[arr[i]] = i
    # return 'No'
    return [-1,-1]



print(twoSum(arr=arr, target=target))