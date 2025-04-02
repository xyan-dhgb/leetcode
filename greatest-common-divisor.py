def kidWithCandies(candies:list[int], extraCandies: int) -> list[bool]:
    maxCandy = max(candies)
    resultArray = []
    
    trueAnswer = "true"
    falseAnswer = "false"
    
    for candy in candies:
        if extraCandies + candy >= maxCandy:
            resultArray.append(True)
        else :
            resultArray.append(False)
    return resultArray

candiesReal = [2,3,5,1,3]
extraCandiesReal = 3

print(kidWithCandies(candiesReal, extraCandiesReal)) 