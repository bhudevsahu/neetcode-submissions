class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countT, countS = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            countT[s[i]] += 1
            countS[t[i]] += 1

        return countS == countT
