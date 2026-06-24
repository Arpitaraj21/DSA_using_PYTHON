arr = [1,2,3,3,4,2,4,5,1,4]

seen = set()

def FirstRepeatingElement(arr):
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
        

print(FirstRepeatingElement(arr))