#https://leetcode.cn/problems/surrounded-regions/
from typing import List
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]




class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        M x N 2d matrics, 
        """
        board = [[0,0,0], [0,0,0]]
        M = len(board)
        N = len(board[0])

        res_board = [[0]*N] * M

        go_layer

        




    def loop_neibours(self, x, y, M, N):
        """ loop through left, up, right, down """

        left = (x-1, y) if x > 0 else None
        up = (x, y-1) if y > 0 else None
        right = (x+1, y) if x < N-1 else None
        down = (x, y+1) if y < M-1 else None

        for res in [left, up, right, down]:
            if res:
                yield res



    def go_layer(self, board, save_block = None, o_list = []) -> List[List[str]]:
        """
        返回下一层的save_block
        """

        M = len(board)
        N = len(board[0])

        next_save_block = []

        # 最外层
        if save_block == None:
            for i,j in self.loop_around(board):
                for x,y in self.loop_neibours(i, j, M, N): 
                    if board[x][y] == 'o':
                        next_save_block.append((x,y))


        # 如果没有直接返回空
        elif save_block == []:
            return [[]]

        else:
            for i,j in save_block:
                pass




    def loop_around(self, board):

        for i in range(len(board)):
            for j in range(len(board[0])):
                yield (i,j)





if __name__ == "__main__":
    s =Solution()
    s.solve(board)
