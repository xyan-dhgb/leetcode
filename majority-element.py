class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        counts = {}
        majority = len(nums) // 2

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > majority:
                return num
        
# Example usage:
# Input: nums = [3,2,3]
# Output: 3

test = Solution()
print(test.majorityElement([3, 2, 3]))  # Output: 3
print(test.majorityElement([2,2,1,1,1,2,2]))  # Output: 2