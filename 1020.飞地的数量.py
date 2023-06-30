from typing import List, Tuple

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        
        self.visited = set()

        M = len(grid)
        N = len(grid[0])

        self.M = M
        self.N = N

        # import ipdb;ipdb.set_trace()


        # visited the edge first
        for (x,y) in self.loop_edge(M, N):
            self.go_through(grid, (x,y))

        num = 0
        for i in range(M):
            for j in range(N):
                if (i,j) not in self.visited:
                    num += grid[i][j]

                # num += self.go_through(grid, (i,j))

        return num

    def loop_edge(self, M, N):

        for i in range(N):
            yield (0,i)

        for j in range(1, M):
                yield (j, N -1)

        for i in range(N-2, -1, -1):
            if M - 1 > 0:
                yield (M -1, i)

        for j in range(M-2, 0, -1):
            if N - 1 > 0:
                yield (j, 0)


    

    def go_through(self, grid, position: Tuple[int, int], current = 0):
        (x,y) = position


        if (x,y) in self.visited:
            self.visited.add((x,y))
            return 0


        if grid[x][y] == 0:
            self.visited.add((x,y))
            return 0

        # if the grid[x][y] == 1
        else:
            for next_step in self.loop_neibours(grid, (x,y)):
                self.visited.add((x,y))
                self.go_through(grid, next_step, current+1)
        return current



        

    def loop_neibours(self, gird, position):

        (x,y) = position

        left = (x, y-1) if y > 0 else None
        right = (x, y+1) if y < self.N-1 else None
        up = (x-1, y) if x > 0 else None
        down = (x+1, y) if x < self.M-1 else None

        for pos in [left, right, up, down]:
            if pos:
                yield pos

        


if __name__ == "__main__":
    grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]

    solution = Solution()
    res = solution.numEnclaves(grid)

    # for res in solution.loop_edge(9, 1):
    print(res)
