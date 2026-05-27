class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
            i+=1
        return False