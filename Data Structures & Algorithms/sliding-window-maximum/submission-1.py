class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        out = []


        # brute force 
        # for idx in range(k-1, len(nums)):
        #     out.append(max(nums[idx-k+1:idx+1]))



        # optimal heap 
        heap = []
        for idx, val in enumerate(nums):
            
            heapq.heappush(heap, (-val, idx) )
            
            while heap[0][1] <= idx-k:
                heapq.heappop(heap)
            
            if idx >= k-1:
                out.append(-heap[0][0])


        return out