class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = defaultdict(int)

        for c in t:
            countT[c] += 1

        l = 0
        res, resLen = [-1, -1], float("infinity")
        need, have = len(countT), 0
        window = defaultdict(int)

        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while need == have:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res

        return s[l:r+1] if resLen != float("infinity") else ""