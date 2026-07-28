class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxL = 0
        numSet = set(nums)

        for num in numSet:
            if num - 1 not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                
                maxL = max(maxL, length)

        return maxL