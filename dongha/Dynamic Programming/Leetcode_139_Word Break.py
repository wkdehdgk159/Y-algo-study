# https://leetcode.com/problems/word-break/
# 139. Word Break (Medium)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1

        for i in range(1, len(s) + 1):
            j = i - 1
            while j >= 0:
                if dp[j] == 1 and s[j:i] in wordDict:
                    dp[i] = 1
                    break
                j -= 1

        if dp[-1] == 1:
            return True
        else:
            return False
        
        # s를 하나하나 나아가면서 특정 구간까지 만들어질 수 있는 가를 확인