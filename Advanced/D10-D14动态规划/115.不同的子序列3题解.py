
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        m, n = len(s), len(t)
        dp = [1]+[0]*n
        for i in range(m):
            for j in range(n-1, -1, -1):
            # for j in range(0, n, 1):
                print(i,j)
                if s[i] == t[j]:
                    dp[j+1] += dp[j]
                    print(i, j, dp)

        print(dp)
        return dp[-1] % (10**9+7)



if __name__ == '__main__':
    solu = Solution()
    s = "rabbbit"
    t = "rabbit"

    # s = "babgbag"
    # t = "bag"
    result = solu.numDistinct(s,t)
    print(result)
