## https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        positive_maximum = nums[0];
        negative_maximum = nums[0];
        maximum = nums[0];

        for i in range(1, len(nums)):
            tmp1 = max(nums[i], positive_maximum * nums[i], negative_maximum * nums[i])
            tmp2 = min(nums[i], positive_maximum * nums[i], negative_maximum * nums[i])
            positive_maximum = tmp1
            negative_maximum = tmp2
            maximum = max(positive_maximum, maximum)
	## 절대값이 큰 음수, 양수 모두 가장 큰 product가 될 후보들이므로 따로 유지해준다.
	## 0에 대한 특수성 고려가 가장 어려웠으나 0이 나올 시 positive, negative maximum을 0으로 초기화하여 handling하였다.
            
        return maximum
        