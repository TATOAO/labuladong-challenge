
# nodes: 0, 1, 2, 3, 4
graph = [[4,3,1],[3,2,4],[],[4],[]]
graph = [[2],[],[1]]
# output:
# [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.graph[-1] = []
        return self.goNext([0])

    def goNext(self, current_path: List[int]) -> List[List[int]]:
        current_node = current_path[-1]
        neibours = self.graph[current_node]

        if len(neibours) == 0:
            return [current_path]
        res = []

        for next_node in neibours:
            new_path = current_path + [next_node]
            res += self.goNext(new_path)

        return res

solution = Solution()

result = solution.allPathsSourceTarget(graph)
print(result)




