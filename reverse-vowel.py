class Solution(object):
    def reverseVowels(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """

        givenStringToList = list(s)
        vowels = set('aeiouAEIOU')
        left, right = 0, len(givenStringToList) - 1

        while left < right:

            while left < right and givenStringToList[left] not in vowels:
                left += 1

            while left < right and givenStringToList[right] not in vowels:
                right -= 1

            givenStringToList[left], givenStringToList[right] = givenStringToList[right], givenStringToList[left]
            left += 1
            right -= 1

        return ''.join(givenStringToList)


# Example usage:
test = Solution()
print(test.reverseVowels("hello"))       # Output: "holle"
print(test.reverseVowels("leetcode"))   # Output: "leotcede"
