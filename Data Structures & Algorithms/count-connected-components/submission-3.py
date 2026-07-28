class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):
            if node in visited:
                return False
            
            visited.add(node)
            
            for n in adj[node]:
                dfs(n)

            return True


        count = 0
        for i in range(n):
            if dfs(i):
                count += 1

        return count