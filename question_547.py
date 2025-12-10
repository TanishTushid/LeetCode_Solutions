class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected) 
        visited = [False]*n

        def dfs(city):
            for nei in range(n):
                if isConnected[city][nei] == 1 and not visited[nei]:
                    visited[nei] = True
                    dfs(nei)

        province = 0
        for city in range(n):
            if not visited[city]:
                visited[city] = True
                dfs(city)
                province += 1
        return province
