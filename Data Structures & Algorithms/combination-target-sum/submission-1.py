class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []
        
        
        def dfs(nums, target, local_res = [], cur_sum=0): 
            
            for i in nums:

                if cur_sum + i == target and sorted(local_res + [i]) not in res: 
                    res.append(sorted(local_res + [i]) )

                elif cur_sum + i > target:
                    continue 
                else:
                    dfs(nums, target, local_res[:] + [i], cur_sum = cur_sum + i )  





        dfs(nums, target)

        print(res)

        return res