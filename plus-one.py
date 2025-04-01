class Solution(object):
    def plusOne(self, digits: list[int]) -> list[int]:
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        stringInitial = ""
        
        for character in digits:
            stringInitial += character
            
        stringToNumber = int(stringInitial)
        
        finalResult = stringToNumber + 1
        
        arrayFinal = []
        numbertoString = str(finalResult)
        
        for result in numbertoString:
            arrayFinal.append(int(result))
            
        print(arrayFinal)