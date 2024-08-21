from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.N = len(board)


        # define iterator group
        self.rows = [set() for _ in range(self.N)]
        self.cols = [set() for _ in range(self.N)]
        self.grid = [[set() for _ in range(3)] for _ in range(3)]

        self.need_to_fill = []
        for i in range(self.N):
            for j in range(self.N):
                n_row_grid = i // 3
                n_col_grid = j // 3

                val = board[i][j]
                self.rows[i].add(val)
                self.cols[j].add(val)
                self.grid[n_row_grid][n_col_grid].add(val)
                if val == '.':
                    self.need_to_fill.append((i,j))

        self.max_filled = len(self.need_to_fill)
        self.finish_puzzle = False

        self.added_path = []

        self.explore(0)
        return self.added_path

    def explore(self, i_step):

        if i_step >= self.max_filled:
            return

        pos = self.need_to_fill[i_step]
        pos_nums = self.get_all_possible_nums(pos)

        if len(self.added_path) == self.max_filled and len(pos_nums) == 1:
            import ipdb;ipdb.set_trace()
            self.finish_puzzle = True
            return


        for num in pos_nums:
            self.fill_one_number(pos, num)

            self.added_path.append(num)
            self.explore(i_step + 1)

            if self.finish_puzzle:
                return
            self.delt_one_number(pos, num)
            self.added_path.pop()
                    

    def fill_one_number(self, pos, num) -> None:
        nrow, ncol = pos
        x,y = self.get_grid(pos)

        self.rows[nrow].add(num)
        self.cols[ncol].add(num)
        self.grid[x][y].add(num)

    def delt_one_number(self, pos, num) -> None:
        nrow, ncol = pos
        x,y = self.get_grid(pos)

        self.rows[nrow].remove(num)
        self.cols[ncol].remove(num)
        self.grid[x][y].remove(num)

    def get_grid(self, pos):
        nrow, ncol = pos
        n_row_grid = nrow // 3
        n_col_grid = ncol // 3

        return (n_row_grid, n_col_grid)

    def get_all_possible_nums(self, pos) -> set:
        all_num = set([ str(_) for _ in range(1,10)])
        nrow, ncol = pos
        x,y = self.get_grid(pos)

        rows_existed = self.rows[nrow]
        cols_existed = self.cols[ncol]
        gird_existed = self.grid[x][y]
        result = all_num - rows_existed - cols_existed - gird_existed
        return result

if __name__ == '__main__':
    solu = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    result  = solu.solveSudoku(board)
    print(result)
