class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        l = 0 
        r = len(nums) - 1

        j_map = {}
        for i in range(len(nums)):
            diff = target - nums[i] 
            if diff in j_map:
                return sorted([i, j_map[diff]])
            else: 
                j_map[nums[i]] = i 

