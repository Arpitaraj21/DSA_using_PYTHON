arr = [10,20,30,40,50]
target = 30
found = False

for num in arr:
    if num == target:
        found = True
        break
    
print(found)