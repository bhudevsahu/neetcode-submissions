class Solution:
    # Time O(n^2), Space: O(1)
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     i = 0
    #     while i < len(nums):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] == nums[j]:
    #                 return True
    #         i+=1
    #     return False

    # Time O(n), Space: O(1)
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
            