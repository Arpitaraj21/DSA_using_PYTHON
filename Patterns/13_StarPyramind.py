def StarPyramid(n):
    for i in range(n):
        # Print spaces
        print(" " * (n - i - 1), end="")

        # Print stars
        print("*" * (2 * i + 1))
StarPyramid(5)