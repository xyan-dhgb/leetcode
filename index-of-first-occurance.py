class Solution(object):
    def strStr(self, haystack:str, needle:str) -> int:
        """
        type haystack: str
        type needle: 
        rtype: int
        """
        
        haystack = haystack.lower()
        needle = needle.lower()
        
        if needle == "" and haystack == "":
            return 0
        
        array_result = []
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                array_result.append(i)
        
        return array_result[0] if len(array_result) > 0 else -1