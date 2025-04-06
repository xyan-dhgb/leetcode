class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(nums) == 0:
            return False
        
        found = set()
        
        for number in nums:
            if number in found:
                return True
            found.add(number)
            
        return False
    

# Example usage:
test = Solution()
print(test.containsDuplicate([1, 2, 3, 1]))  # Output: True
print(test.containsDuplicate([1,2,3,4]))  # Output: False