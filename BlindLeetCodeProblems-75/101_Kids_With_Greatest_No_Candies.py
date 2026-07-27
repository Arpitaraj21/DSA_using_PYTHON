candies = [2, 3, 5, 1, 3]
extraCandies = 3
result = []

def kidsWithCandies( candies, extraCandies: int):
    max_candies = max(candies)
    for candy in candies:
        if candy + extraCandies >= max_candies:
            result.append("True")
        else:
            result.append("False")
    
    return result


print(kidsWithCandies(candies=candies, extraCandies=extraCandies))