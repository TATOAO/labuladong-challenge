
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        self.N = n

        self.recorded_iterator = {}

        self.all_possible_pos([1])
        temp = self.sub([])
        for _ in range(self.N-1):
            temp_2 = []
            for path in temp:
                temp_2 += self.sub(path)
            temp = temp_2

        result = []
        for result_queens in temp:

            default_map = []
            for nrow, queen_col in enumerate(result_queens):
                row_str = ''.join(['.'] * (queen_col)) + 'Q' + ''.join(['.'] * (n - queen_col - 1))
                default_map.append(row_str)

            result.append(default_map)
        return result


    def sub(self, prevoius_queens: List[int]) -> List[List[int]]:


        result = []
        all_possible = self.all_possible_pos(prevoius_queens)
        for i in all_possible:
            result += [prevoius_queens + [i] ]

        return result

    def all_possible_pos(self,  previous_queens):
        vertical_set = frozenset(previous_queens)

        vertical_path = tuple(previous_queens)

        if vertical_set not in self.recorded_iterator:

            path_length = len(previous_queens)
            diagnal_positive = [previous_queens[i] + (path_length - i ) 
                                for i in range(path_length)
                                if previous_queens[i] + (path_length - i ) < self.N
                                ]

            diagnal_negative = [previous_queens[i] - (path_length - i ) 
                                for i in range(path_length)
                                if previous_queens[i] - (path_length - i ) >= 0
                                ]

            all_line = set([_ for _ in range(self.N) ]) - set(diagnal_positive) - vertical_set - set(diagnal_negative)

            self.recorded_iterator[vertical_path] = all_line

        return self.recorded_iterator[vertical_path]

if __name__ == '__main__':
    solu = Solution()

    result  = solu.solveNQueens(4)

    print(result)





