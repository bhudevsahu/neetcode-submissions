class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countS = defaultdict(int)

        l = 0
        res = 0

        for r in range(len(s)):
            c = s[r]
            countS[c] += 1

            if (r-l+1) - max(countS.values()) > k:
                countS[s[l]] -= 1
                l += 1
            
            res = max(((r-l+1)), res)
        
        return res