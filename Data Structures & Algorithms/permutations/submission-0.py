class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perm_length = len(nums)
        out = []
        def perm(candidates, res):
            
            if len(res) == perm_length:
                out.append(res.copy())
                return

            for i in candidates:
                
            
                res.append(i)
          

                can_copy = candidates.copy()
                can_copy.remove(i)

                perm(can_copy, res)

                res.pop()

        

        perm(nums, [])

        return out
