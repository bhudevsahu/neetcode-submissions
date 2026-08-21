class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        visited = set()
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        count = 0

        def dfs(node):
            if node in visited:
                return False
            
            visited.add(node)

            for n in adj[node]:
                dfs(n)
            
            return True

        for n in range(n):
            if dfs(n):
                count += 1

            
        return count