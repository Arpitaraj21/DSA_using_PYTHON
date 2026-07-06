def Inverted_Right_Pyramind(n):
    for i in range(n, 0, -1):
        for j in range(i-1, 0, -1):
            print("*", end="")
        print()

Inverted_Right_Pyramind(5)