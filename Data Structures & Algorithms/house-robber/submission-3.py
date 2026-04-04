class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[-1]

        if len(nums) == 2:
            return max(nums)


        dp = [0 for x in range(len(nums))]


        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])


        return max(dp[-1], dp[-2])
