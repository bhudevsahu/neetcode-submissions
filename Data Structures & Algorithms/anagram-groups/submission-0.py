class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        map = {}

        for i in range(len(strs)):
            if strs[i] not in map:
                anagrams = [strs[i]]
                for j in range(i+1, len(strs)):
                    if self.isAnagram(strs[i], strs[j]):
                        anagrams.append(strs[j])
                        map[strs[j]] = True
                result.append(anagrams)
            map[strs[i]] = True
        
        return result


    



    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT