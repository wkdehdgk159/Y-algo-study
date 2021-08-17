# https://leetcode.com/problems/jump-game/
# 55. Jump Game (Medium)

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_index = 0
        tmp = 0


        while max_index < len(nums) - 1:
            tmp = max_index
            for i in range(max_index, max_index + nums[max_index] + 1):
                if max_index + nums[max_index] < i + nums[i]:
                    max_index = i
                if max_index + nums[max_index] >= len(nums) - 1:
                    return True
            if max_index == tmp:
                break
        
        # 현재 index에서 갈 수 있는 범위 내에서 그 다음으로 제일 멀리 갈 수 있는 index를 max_index로 갱신 

        if max_index >= len(nums) - 1:
            return True
        else:
            return False