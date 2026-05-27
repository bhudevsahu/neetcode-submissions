class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        range_nums = []

        for i in range(len(nums)+1):
            range_nums.append(i)

        res = 0
        for num in range_nums:
            if num not in nums:
                return num
        
        return res