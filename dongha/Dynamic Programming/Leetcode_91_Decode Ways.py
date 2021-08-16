# https://leetcode.com/problems/decode-ways/
# 91. Decode Ways (Medium)

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1

        if int(s[0]) == 0:
            return 0

        for i in range(2, len(s) + 1):
            if 0 < int(s[i-1]) and int(s[i-1]) <= 9:
                dp[i] = dp[i - 1]
            if 10 <= int(s[i-2:i]) and int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]
                
        return dp[-1]

	# 주어진 숫자를 그대로 더하는 경우는 dp[i-1]을 그대로 받고, 두자리수가 부합하는 경우 dp[i-2] 만큼의 케이스가 더 생기는 것