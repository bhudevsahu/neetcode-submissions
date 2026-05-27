class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        length = len(nums)
        for i in range(length):
            val = nums[i]

            l, r = i+1, length-1
            target = -1 * val

            while l < r:

                if nums[l] + nums[r] < target:
                    l+=1
                elif nums[l] + nums[r] > target:
                    r-=1
                else:
                    res.add(tuple([val, nums[l], nums[r]]))
                    l+=1
                    r-=1
        
        return [list(v) for v in res]

        