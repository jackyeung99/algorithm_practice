class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        

        
        prefixSums = { 0 : 1 }
        res = 0

        cum_sum = 0
        for i in nums: 
            cum_sum += i
            diff = cum_sum - k
            
            
            res += prefixSums.get(diff, 0)
            prefixSums[cum_sum] = 1 + prefixSums.get(cum_sum, 0)

        return res


        