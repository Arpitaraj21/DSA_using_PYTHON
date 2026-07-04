# structure

# def function_name(parameter):
#     # base case
#     if condition:
#         return value
    
#     # recursive case
#     return function_name(modified_condition)



# 1) print numbers from N to 1


def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n-1)


print_numbers(5)