class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minVal = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                minVal = min(nums[l], minVal)
                break

            m = (l+r) // 2
            minVal = min(nums[m], minVal)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return minVal