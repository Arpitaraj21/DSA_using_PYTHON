def InvertedNumberRightPyramid(n):
    for i in range(n-1, 0, -1):
        for j in range(i+1):
            print(j+1,end="")
        print()
    

InvertedNumberRightPyramid(5)