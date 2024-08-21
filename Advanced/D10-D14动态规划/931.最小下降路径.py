from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        self.matrix = matrix
        self.N, self.M = len(matrix), len(matrix[0])

        self.invser_path_min_sum = [[-1] * self.M for _ in range(self.N-1)]

        self.invser_path_min_sum.append(matrix[-1])


        for row in range(self.N-2, -1, -1):
            for column in range(0, self.M):
                current_value = self.matrix[row][column]
                self.invser_path_min_sum[row][column] = current_value +\
                        self.get_min_next_row_sum(row, column)


        return min(self.invser_path_min_sum[0])
        
    def get_min_next_row_sum(self, i, j) -> int:

        left = max(0, j - 1)
        right = min(j + 2, self.M)

        return min(self.invser_path_min_sum[i+1][left:right])


if __name__ == '__main__':
    solu = Solution()
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    matrix = [[-19, 57], [-40, -5]]
    matrix = [[17,82],[1,-44]]

    result = solu.minFallingPathSum(matrix)

    print(result)
    
