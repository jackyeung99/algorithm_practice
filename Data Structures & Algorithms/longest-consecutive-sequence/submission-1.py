class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0 
            
        hash_set = set()
        for i in range(len(nums)):
            hash_set.add(nums[i])
        
        
        max_streak = 1
        for i in range(len(nums)): 
            val = nums[i]
            if val - 1 in hash_set:
                continue

            streak = 1
            while True:
                if val + 1 in hash_set:
                    streak += 1 
                    val += 1
                else:
                    break 

            max_streak = max(max_streak, streak)


        return max_streak


            
