class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        total_sum = 0

        for num in range(len(nums) + 1):
            total_sum += num

        return total_sum - nums_sum