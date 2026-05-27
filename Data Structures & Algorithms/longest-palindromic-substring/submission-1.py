class Solution:

    def __init__(self):
        self.res = ""
        self.resLen = 0
    
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            self.findPali(s, i, i)
            self.findPali(s, i, i+1)
        
        return self.res


    
    def findPali(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > self.resLen:
                self.res = s[l:r+1]
                self.resLen = (r - l + 1)

            l -= 1
            r += 1