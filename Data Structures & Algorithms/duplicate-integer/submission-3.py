class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # The map is to keep track of occurence of each number
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1

        for v in map.values():
            if v > 1:
                return True

        return False