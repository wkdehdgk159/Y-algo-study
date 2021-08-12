# https://leetcode.com/problems/longest-increasing-subsequence/submissions/
# 300. Longest Increasing Subsequence (Medium)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        candidate = [1]
        for i in range(1, len(nums)):
            j = i - 1
            tmp = [1]
            while j >= 0:
                if nums[j] < nums[i]:
                    tmp.append(candidate[j] + 1)
                j -= 1
            check = 0
            candidate.append(max(tmp))

        return max(candidate)
    
    ## candidate[i]는 nums[i]가 마지막인 subsequence의 최대 길이를 뜻한다. 자신 앞의 nums 요소들을 다 살피며 자신이 그 요소보다 크다면 이러면 n^2이라 구글링 해봤는데 lower bound 써야한다 하더라..