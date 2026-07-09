arr = [1, 2, 3,1]

# Function to check for duplicates using set
def containsDuplicate(nums):
    # Store unique elements in a set
    unique = set(nums)

    # If set has fewer elements, duplicates existed
    return len(unique) < len(nums)

# Sample input
nums = [1, 2, 3, 1]

# Call the function and print result
print("true" if containsDuplicate(nums) else "false")




# ********* This approach is best when we want to return the duplicate number
# def ContainDuplicate(arr):
#     seen = set()
#     for i in range(len(arr)):
#         if arr[i] in seen:
#             return "Contains Duplicate"
            
#         seen.add(arr[i])
    
#     return False


# print(ContainDuplicate(arr))