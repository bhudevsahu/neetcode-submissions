class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        visited = set()
        cycle = set()
        res = []

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

            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)

            return True

        
        for c in range(numCourses):
            if not dfs(c):
                return []

        return res

            

            