# 1,5,10 -  12




class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        coins.sort()
        
        # min_coins = float("inf")
        amount_arr = [float("inf")]*(amount+1)
        amount_arr[0] = 0

        print(amount, coins, len(amount_arr))
        for i in range(1, len(amount_arr)):
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break
                amount_arr[i] = min(amount_arr[i], 1 + amount_arr[diff])
            # print(amount_arr[:i+1])







        
        if amount_arr[-1] == float("inf"):
            min_coins = -1
        else:
            min_coins = amount_arr[-1]
        return min_coins
        