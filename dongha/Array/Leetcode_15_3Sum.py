# https://leetcode.com/problems/3sum/
# 15. 3Sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        #빈 리스트 예외처리
        if len(nums) < 3:
            return ans

        nums.sort()
        dupli = nums[len(nums) - 1] + 1
        lefttmp = nums[0] - 1
        righttmp = nums[len(nums) - 1] + 1

        for i in range(0, len(nums)):
            left = i + 1
            right = len(nums) - 1

            # 중복 제거
            if dupli == nums[i]:
                continue

            # 양수로만 이루어진 케이스는 절대 있을 수 없음
            if nums[i] > 0:
                break

            dupli = nums[i]

            while left < right:
                threesum = nums[i] + nums[left] + nums[right]
                if threesum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    lefttmp = nums[left]
                    righttmp = nums[right]
                    
                    # 중복 제거될 때 까지 이동
                    while lefttmp == nums[left] and left < right:
                        left = left + 1
                    while righttmp == nums[right] and left < right:
                        right = right - 1
                        
                elif threesum < 0:
                    left = left + 1

                elif threesum > 0:
                    right = right - 1
                    
        return ans