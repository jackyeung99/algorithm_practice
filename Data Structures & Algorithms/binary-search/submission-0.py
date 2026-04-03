class Solution:
    def search(self, nums: List[int], target: int) -> int:
        


        def bfs(l , r, nums, target):

            if l > r:
                return -1

            pivot = (r + l) // 2

            if target == nums[pivot]: 
                return pivot
            elif target > nums[pivot]: 
                return bfs(pivot+1, r, nums, target)
            else: 
                return bfs(0, pivot-1, nums, target)


        
        return bfs(0, len(nums)-1, nums, target)