class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}


        for i in nums: 
            freq[i] = freq.get(i, 0) + 1


        sorted_freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)

        return [ i for i,j in sorted_freq[:k]]