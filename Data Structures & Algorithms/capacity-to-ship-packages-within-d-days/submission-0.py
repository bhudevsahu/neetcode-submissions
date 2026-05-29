# Complexity: T: O(nlogm), S: O(1). n = Number of weights; m = Sum of all the weights
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            ships, curCap = 1, cap
            for w in weights:
                if curCap - w < 0:
                    ships += 1
                    curCap = cap
                curCap -= w
            return ships <= days
        
        while l <= r:
            cap = (l + r) // 2            
            if canShip(cap):
                r = cap - 1
                res = min(cap, res)
            else:
                l = cap + 1
        
        return res