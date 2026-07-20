class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        cycle = set()

        for c, p in prerequisites:
            preMap[c].append(p)

        def dfs(c):
            if c in cycle:
                return False

            if preMap[c] == []:
                return True

            cycle.add(c)
            for crs in preMap[c]:
                if not dfs(crs):
                    return False

            preMap[c] = []
            cycle.remove(c)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True