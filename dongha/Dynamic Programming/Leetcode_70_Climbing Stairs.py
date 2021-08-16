# https://leetcode.com/problems/climbing-stairs/submissions/
# 70. Climbing Stairs (Easy)

class Solution:
    def climbStairs(self, n: int) -> int:
        fibo = [0 for i in range(46)]
        fibo[0] = 1
        fibo[1] = 2

        for i in range(n - 1):
            fibo[i + 2] = fibo[i] + fibo[i + 1]
            
        # 케이스를 쭉 써내려다 보니 피보나치여서 이렇게 했다. 왜 피보나치가 나올 까 생각해보니 경우의 수가 두 단계 전의 경우의 수에서 두칸을 올라오는 경우 + 한 단계 전의 경우의 수에서 한칸을 올라오는 경우이기 때문

        return fibo[n - 1]