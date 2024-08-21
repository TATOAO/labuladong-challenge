
from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        N = len(books)
        heights = []
        widths = []

        for i in range(N):
            width, height = books[i]
            widths.append(width)
            heights.append(height)
        dp = [100000] * N
        dp[0] = heights[0]


        for i in range(N):
            width_left = shelfWidth - widths[i]
            for j in range(i-1,0,-1):
                print(j)
                height_gain = max(heights[j:i])
                width_left -= widths[j]
                if width_left < 0:
                    break
                dp[i] = min(dp[i], dp[i] + height_gain)

            import ipdb;ipdb.set_trace()
        print(dp)
        return dp[-1]

def main():
    solu = Solution()

    books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
    shelfWidth = 4
    answer = solu.minHeightShelves(books, shelfWidth)
    print(answer)
    

if __name__ == "__main__":
    main()

