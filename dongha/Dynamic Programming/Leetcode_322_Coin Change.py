# https://leetcode.com/problems/coin-change/
# 322. Coin Change (Medium)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort()
        dp = [amount + 1 for i in range(amount + 1)]
        dp[0] = 0

        for i in range(1, amount + 1):
            tmp = [amount + 1]
            for coin in coins:
                if coin > i:
                    break
                tmp.append(dp[i - coin] + 1) 
                #이전 케이스들 중 동전 하나를 더 더하는 느낌
            dp[i] = min(tmp)

        if dp[amount] <= amount:
            return dp[amount]
        else:
            return -1