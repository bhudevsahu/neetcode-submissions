class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        visited = set()
        cycle = set()

        for pre, crs in prerequisites:
            preMap[pre].append(crs)

        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visited:
                return True

            cycle.add(crs)
            for c in preMap[crs]:
                if not dfs(c):
                    return False

            visited.add(crs)
            cycle.remove(crs)
            return True

        
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True