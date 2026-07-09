def sum_of_digits(n):
    if n == 0:
        return 0
    
    Digit = sum_of_digits(n//10)
    sumOfDigit += Digit;
    return sumOfDigit

print(sum_of_digits(123))