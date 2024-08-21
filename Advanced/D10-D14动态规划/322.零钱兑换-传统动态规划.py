from typing import List

class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.records = {}

        self.records[0] = 0

        return self.dp(coins, amount)


    def dp(self, coins: List[int], amount: int) -> int:
        if amount in self.records:
            return self.records[amount]

        if amount < 0 :
            return -1


        pending_min = []
        for coin in coins:
            coins_need = self.dp(coins, amount - coin) + 1
            if coins_need >= 1:
                pending_min.append(coins_need)

        if len(pending_min) == 0 :
            self.records[amount] = -1
            return -1

        result = min(pending_min)
        self.records[amount] = result
        return result

if __name__ == "__main__":
    solution = Solution()
    coins = [1,2,5]
    # coins = [2147483647]
    # coins = [186,419,83,408]
    amount = 100
    # amount = 6249
    result = solution.coinChange(coins, amount)
    print(result)
    

