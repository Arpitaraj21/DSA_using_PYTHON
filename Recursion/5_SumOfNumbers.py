def sum_of_numbers(n):
    if n == 0:
        return 0
    small_sum = sum_of_numbers(n-1)
    return small_sum + n


print(sum_of_numbers(5))