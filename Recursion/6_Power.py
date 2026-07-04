def power_of_number(n):
    if n == 0:
        return 1
    small_power = power_of_number(n-1)
    return small_power * 2

print(power_of_number(5))