class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        

        max_streak = 0
        cur_streak = 0 

        for i in nums: 
            if i == 1:
                cur_streak += 1
                max_streak = max(max_streak, cur_streak)
            else:
                cur_streak = 0


        return max_streak
