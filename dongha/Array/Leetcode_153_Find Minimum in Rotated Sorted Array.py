## https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/
## 153. Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        head = 0
        tail = len(nums) - 1
        middle = (head + tail) / 2
        
        # 1개의 element를 가진 case
        if tail == 0:
            return nums[0]
        
        #같아지는 경우는 그 위치가 최소값
        while head != tail:
        
            middle = int((head + tail) / 2)
            
            if nums[middle] > nums[middle + 1]:
                return nums[middle + 1]
            
            #지금 middle 값이 tail값보다 크다면 오른쪽에 최소값이 존재할 것.
            else:
                if nums[middle] > nums[tail]:
                    head = middle
                else:
                    tail = middle
            
        return nums[middle]