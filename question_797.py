class Solution(object):
    def allPathsSourceTarget(self, graph):
        target = len(graph) -1
        result = []
        def dfs(node, path):
            if node == target:
                result.append(list(path))
                return
            for nei in graph[node]:
                path.append(nei)
                dfs(nei, path)
                path.pop()
        dfs(0,[0])
        return result 
        
