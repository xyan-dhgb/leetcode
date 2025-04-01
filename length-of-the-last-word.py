class Solution(object):
    def lengthOfLastWord(self, s:str) -> int:
        """
        :type s: str
        :rtype: int
        """
        word_split = s.split()
        
        return len(word_split[-1]) if word_split else 0