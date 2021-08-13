# https://leetcode.com/problems/house-robber-ii/
# 213. House Robber II (Medium)

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp1 = [0 for i in range(len(nums))]
        dp2 = [0 for i in range(len(nums))]
        
        if len(nums) == 1:
            return nums[0]
        
        dp1[0] = 0
        dp1[1] = nums[0]

        dp2[0] = 0
        dp2[1] = nums[1]

        for i in range(2, len(nums)):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i - 1])

        for i in range(2, len(nums)):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])


        return max(dp1[-1], dp2[-1])

	#첫번째 집을 포함하는 경우와 아닌 경우를 나눠서 생각