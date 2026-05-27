class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)


        def dfs(node):
            if node in visited:
                return 0

            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
            
            return 1
        
        count = 0
        for i in range(n):
            count += dfs(i)
        
        return count