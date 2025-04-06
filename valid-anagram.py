class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        for word in s:
            if word in t:
                t = t.replace(word, '', 1)
            else:
                return False
        return True
    
test = Solution()
print(test.isAnagram("anagram", "nagaram"))  # Output: True
print(test.isAnagram("rat", "car"))  # Output: False    