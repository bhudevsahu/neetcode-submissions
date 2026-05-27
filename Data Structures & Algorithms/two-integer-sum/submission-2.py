class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {value: index for index, value in enumerate(nums)}

        for i in range(len(nums)):
            num_2 = (target - nums[i])
            if num_2 in d and i != d[num_2]:
                return [i, d[num_2]]
        
        return []