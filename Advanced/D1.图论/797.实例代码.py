import collections
from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result=list()
        dq=list()
        n=len(graph)
        def dfs(i):
            if(i==n-1):
                result.append(dq+[i])
            dq.append(i)
            for j in graph[i]:
                dfs(j)
            dq.pop()
        dfs(0)
        return result
# nodes: 0, 1, 2, 3, 4
graph = [[4,3,1],[3,2,4],[],[4],[]]

solution = Solution()
result = solution.allPathsSourceTarget(graph)
print(result)


