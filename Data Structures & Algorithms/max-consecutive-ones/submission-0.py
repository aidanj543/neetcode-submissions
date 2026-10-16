class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k = 0
        k_max = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                k +=1
                if k>= k_max:
                    k_max = k
            elif nums[i] == 0:
                k =0
        return k_max

