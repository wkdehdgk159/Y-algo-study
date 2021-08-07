# https://leetcode.com/problems/container-with-most-water/submissions/
# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            container = (right - left) * min(height[left], height[right])
            ans = max(ans, container)
            
            # 양쪽에서 작은 친구를 옮겨야지 더 커질 가능성이 있다.
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return ans