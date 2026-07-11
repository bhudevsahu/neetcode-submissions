class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}

        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        maxElement = nums[0]
        for k, v in map.items():
            if v > map[maxElement]:
                maxElement = k
        
        return maxElement