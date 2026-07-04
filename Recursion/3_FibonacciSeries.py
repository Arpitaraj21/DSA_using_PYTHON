def fibonacciSeries(n):
    if n<=1:
        return n
    
    return fibonacciSeries(n-1) + fibonacciSeries(n-2)

print(fibonacciSeries(5))