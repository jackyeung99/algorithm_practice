class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        


        all_sub = [[], ]
        def bt(nums_left, res=[]): 
            
            # print(nums_left)
            if not nums_left:    
                return 
            
            for i in nums_left:

                if len(res) == 0 or i > res[-1]:
                    copy = nums_left[:]
                    
                    res_copy = res[:]
                    res_copy.append(i)
                    all_sub.append(res_copy[:])

                    copy.remove(i)
                
                    bt(copy[:], res_copy[:])

            

        bt(nums)
        return all_sub 

