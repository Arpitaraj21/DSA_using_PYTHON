class Solution:
    # Function to print Pattern 8
    def pattern8(self, N):
        # Outer loop for rows
        for i in range(N):

            # Print leading spaces
            for j in range(i):
                print(" ", end="")

            # Print stars
            for j in range(2 * N - (2 * i + 1)):
                print("*", end="")

            # Print trailing spaces
            for j in range(i):
                print(" ", end="")

            # Move to next row
            print()

if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.pattern8(N)
