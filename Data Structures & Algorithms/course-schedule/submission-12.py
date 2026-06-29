class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        visited = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(c):
            if c in visited:
                return False
            
            if preMap[c] == []:
                return True

            visited.add(c)
            for crs in preMap[c]:
                if not dfs(crs):
                    return False
                
            visited.remove(c)
            preMap[c] == []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
