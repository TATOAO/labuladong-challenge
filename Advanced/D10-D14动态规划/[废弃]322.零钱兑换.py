from typing import List

class Solution:

    records = {}
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        self.coins = sorted(coins, key = lambda x: -x)

        self.records = {}

        for coin in coins:
            self.records[coin] = 1

        self.min_coin = min(coins)
        self.max_possible_cnt = amount // self.min_coin
        result = self.sub_coin_change(0, amount)
        return result


    def sub_coin_change(self, already_used: int, amount_left) -> int:
        print(already_used, amount_left)

        if amount_left < self.min_coin or already_used > self.max_possible_cnt:
            return -1
        

        if amount_left in self.records:
            coin_cnt_in_records = self.records[amount_left]
            if coin_cnt_in_records == -1:
                return -1
            else:
                return already_used + coin_cnt_in_records


        
        possible_results = []
        for next_coin in self.coins:
            left = amount_left - next_coin

            current_result = self.sub_coin_change(already_used+1, left)
            if current_result == -1:
                continue
            
            possible_results.append(current_result)

        if len(possible_results) == 0:
            return -1
        else:
            min_result = min(possible_results)
            self.records[amount_left] = min_result 
            return min_result

if __name__ == "__main__":
    solution = Solution()
    coins = [1,2,5]
    coins = [2147483647]
    coins = [186,419,83,408]
    amount = 11
    amount = 6249
    result = solution.coinChange(coins, amount)
    print(result)
    

