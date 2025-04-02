firstString = "abcd"
secondString = "pq"


if len(firstString) == len(secondString):
    mergedString = ''.join(a + b for a, b in zip(firstString, secondString))
    
elif len (firstString) < len(secondString):
    mergedString = ''.join(a + b for a, b in zip(firstString, secondString)) + secondString[len(firstString)-0:] 
elif len(firstString) > len(secondString):
    mergedString = ''.join(a + b for a, b in zip(firstString, secondString)) + firstString[len(secondString)-0:]
    
print(mergedString)