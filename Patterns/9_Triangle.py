def print_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()

print_triangle(5)