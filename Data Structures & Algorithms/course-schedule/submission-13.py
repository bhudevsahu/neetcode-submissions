class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        cycle = set()
        visited = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(c):
            if c in cycle:
                return False
            
            if c in visited:
                return True

            cycle.add(c)
            for crs in preMap[c]:
                if not dfs(crs):
                    return False
                
            cycle.remove(c)
            visited.add(c)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
