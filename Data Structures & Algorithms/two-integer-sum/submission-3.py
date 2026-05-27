class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            first = target - num
            if first in map:
                return [map[first], i]
            else:
                map[num] = i