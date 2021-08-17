# https://leetcode.com/problems/unique-paths/
# 62. Unique Paths (Medium)

import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(math.factorial(m + n - 2) / (math.factorial(m - 1) * math.factorial(n - 1)))
    
    #아니 이건 누가봐도 조합쓰는 거 아닌가... 왜 DP지 
    #라고 생각해서 검색해보니 초딩때 문제푸는 방법찾기에서 나온 것처럼 하면 DP 맞더라