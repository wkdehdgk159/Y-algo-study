# https://leetcode.com/problems/search-in-rotated-sorted-array/
# 33. Search in Rotated Sorted Array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        head = 0
        tail = len(nums) - 1

        while head <= tail:

            middle = int((head + tail) / 2)

            if nums[middle] == target:
                return middle

            elif nums[head] <= nums[middle]:
                
                #nums[head]나 nums[tail] 자체가 target일 가능성을 고려하여 등호를 넣어준다.
                if nums[head] <= target and target < nums[middle]:
                    tail = middle - 1
                else:
                    head = middle + 1

            elif nums[middle] <= nums[tail]:
                if nums[middle] < target and target <= nums[tail]:
                    head = middle + 1
                else:
                    tail  = middle - 1
                    
        return -1