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
        self.can_usage_num = {str(i):9 for i in range(1,10)}
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
                else:
                    self.can_usage_num[val] -= 1

        self.max_filled = len(self.need_to_fill)
        self.finish_puzzle = False

        self.explored = {}
        self.explore()

        for pos in self.explored:
            x,y = pos
            board[x][y] = self.explored[pos]

        return 

    def find_the_min_next_step(self):
        
        self.all_possible_nums = {
                pos: self.get_all_possible_nums(pos)
                for pos in self.need_to_fill}

        self.need_to_fill.sort(key = lambda x:  float('inf') if x in self.explored else len(self.all_possible_nums[x]))


    def explore(self):

        self.find_the_min_next_step()

        pos = self.need_to_fill[0]


        all_possible_num = self.all_possible_nums[pos]

        if len(self.explored) == len(self.need_to_fill):
            self.finish_puzzle = True
            return

        if pos in self.explored:
            return

        for next_num in all_possible_num:
            self.fill_one_number(pos, next_num)
            self.explored[pos] = next_num
            self.explore()
            if self.finish_puzzle:
                return
            self.delt_one_number(pos, next_num)
            self.explored.pop(pos)

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
        all_num = set([str(_) for _ in range(1,10)])
        nrow, ncol = pos
        x,y = self.get_grid(pos)


        for num in self.can_usage_num:
            if self.can_usage_num[num] <= 0:
                return set()

        rows_existed = self.rows[nrow]
        cols_existed = self.cols[ncol]
        gird_existed = self.grid[x][y]
        result = all_num - rows_existed - cols_existed - gird_existed
        return result

if __name__ == '__main__':
    solu = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]


    board = [[".",".",".","2",".",".",".","6","3"],["3",".",".",".",".","5","4",".","1"],[".",".","1",".",".","3","9","8","."],[".",".",".",".",".",".",".","9","."],[".",".",".","5","3","8",".",".","."],[".","3",".",".",".",".",".",".","."],[".","2","6","3",".",".","5",".","."],["5",".","3","7",".",".",".",".","8"],["4","7",".",".",".","1",".",".","."]]
    result  = solu.solveSudoku(board)
    print(board)
