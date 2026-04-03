class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []

        nums.sort()
        
        
        def dfs(start, local_res = [], cur_sum=0): 
            if cur_sum == target:
                res.append(local_res.copy())
                return

            for i in range(start, len(nums)):
                # if i > start and nums[i] == nums[i - 1]:
                #     continue
                
                if nums[i] + cur_sum > target:
                    return 
                
                
                local_res.append(nums[i])

                dfs(i, local_res, cur_sum + nums[i])

                local_res.pop()




        dfs(0)

        return res