class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        res = 0

        while l <= r:
            m = (l + r) // 2
            if m**2 < x:
                l = m + 1
                res = m
            elif m**2 > x:
                r = m - 1
            else:
                res = m
                break

        return res