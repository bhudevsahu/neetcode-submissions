class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countS = defaultdict(int)
        l = 0
        res = 0
        maxF = 0
        for r in range(len(s)):
            countS[s[r]] += 1
            maxF = max(maxF, countS[s[r]])

            while (r - l + 1) - maxF > k:
                countS[s[l]] -= 1
                l += 1
            
            res = max(res, (r-l+1))
        
        return res