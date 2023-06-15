#https://leetcode.cn/problems/surrounded-regions/
from typing import List, Tuple, Iterable
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]




class Solution:


    def solve(self, board: List[List[str]]) -> List[List[str]]:
        """
        Do not return anything, modify board in-place instead.
        M x N 2d matrics, 


        [ 
          [(0,0), (0,1), (0,2)],
          [(1,0), (1,1), (1,2)]
        ]

        2 X 3 matrics

        """
        M = len(board)
        N = len(board[0])

        self.M = M
        self.N = N
        self.path_explored = []


        res_board = [['X' for i in range(N)] for j in range(M)]

        all_o_list = []

        for x,y in self.index_loop_outside(M, N):

            o_list = self.go_through_all_connected_island(board, x, y)

            all_o_list += o_list

        print(all_o_list)


        for x,y in all_o_list:
            res_board[x][y] = 'O'

        return res_board
            

    def loop_neibours(self, x, y):
        """ loop through left, up, right, down """

        M = self.M
        N = self.N

        left = (x, y-1) if y > 0 else None
        up = (x-1, y) if x > 0 else None
        right = (x, y+1) if y < N-1 else None
        down = (x+1, y) if x < M-1 else None

        for res in [left, up, right, down]:
            if res in self.path_explored:
                continue

            if res:
                yield res


    def go_through_all_connected_island(self, board, x, y):
        """
        start from (x,y) in board, return all "o" positions, and all explored positions
        """

        o_positions = []

        if (x,y) in self.path_explored:
            return o_positions

        elif board[x][y] != 'O':
            self.path_explored.append((x,y))
            return o_positions

        else:
            o_positions.append((x,y))
            self.path_explored.append((x,y))

            for x1, y1 in self.loop_neibours(x,y):
                o_p = self.go_through_all_connected_island(board, x1,y1) 
                o_positions += o_p


            return o_positions


    def index_loop_outside(self, M, N) -> Iterable[Tuple[int, int]]:
        """
        从 (0,0) 开始， 
        向右, (0,0) .. (0, N-1)
        向下, (1, N-1) .. (M-1, N-1)
        向左, (M-1, N-2) ... (M-1, 0)
        向上, (M-2, 0) .. (1, 0)

        """


        for i in range(N):
            yield (0, i)

        for j in range(M -1):
            yield(j+1, N-1)

        for i in range(N - 1, 0, -1):
            yield(M - 1, i - 1)

        for j in range(M-1, 1, -1):
            yield(j - 1, 0)







if __name__ == "__main__":

    board = [
                ["X","X","X","X","X","O"], 
                ["X","O","O","O","O","X"],
                ["O","X","O","X","X","X"],
                ["O","X","O","X","X","X"],
                ["O","X","O","X","X","X"],
                ["O","O","O","X","O","X"],
                ["O","X","X","X","X","X"],
                ["O","X","X","X","X","X"],
            ]

    board = [
                ["X","X","X","X"],
                ["X","O","O","X"],
                ["X","X","O","X"],
                ["X","O","X","X"]
            ]

    s =Solution()

    result = s.solve(board)

    print(result)
    
    

    # print([i for i in s.loop_neibours(0,1) if print(s.path_explored) == None])


    # res = s.go_through_all_connected_island(board, 0, 0)
    # print(res)



