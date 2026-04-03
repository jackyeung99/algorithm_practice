class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n

        # left[i] = product of nums[0..i-1]
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]

        # right[i] = product of nums[i+1..n-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        # result
        return [left[i] * right[i] for i in range(n)]