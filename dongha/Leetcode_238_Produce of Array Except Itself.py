class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        output1 = []
        output2 = []


        tmp = 1
        for i in range(len(nums)):
            output1.append(tmp)
            tmp = tmp * nums[i]
        #자기 자신의 왼쪽 원소들의 곱

        tmp = 1
        for i in range(len(nums)):
            output2.insert(0, tmp) 
            # output2에 처음들어오는 원소가 nums의 맨 마지막 원소를 다루므로 맨 앞에 삽입
            # 그러나 그냥 append하고 아래 곱해주는 과정에서의 index를 다루는 게 시간효율성에서 더 앞섰다.
            tmp = tmp * nums[len(nums) - i - 1]
        #자기 자신의 오른쪽 원소들의 곱

        for i in range(len(nums)):
            tmp = output1[i] * output2[i]
            output.append(tmp)

        return output