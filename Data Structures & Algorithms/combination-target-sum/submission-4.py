class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(cur, i, total):
            if total == target:
                res.append(cur.copy())
                return

            if total > target or i >= len(nums):
                return

            cur.append(nums[i])
            dfs(cur, i, total + nums[i])
            cur.pop()
            dfs(cur, i + 1, total)

        dfs([], 0, 0)
        return res