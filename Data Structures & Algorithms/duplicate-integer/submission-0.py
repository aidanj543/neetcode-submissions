class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h_map = {}
        hasDuplicate = False
        for i in range(len(nums)):
            if nums[i] in h_map:
                hasDuplicate = True
            else:
                h_map[nums[i]] = i
        return hasDuplicate
        