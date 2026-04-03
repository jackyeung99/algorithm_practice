import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
    
        heap = stones
        heapq.heapify_max(heap)

        while len(heap) > 1:

            # print(heap)

            s1 = heapq.heappop_max(heap)
            s2 = heapq.heappop_max(heap)

            if not s1-s2 == 0:
                heapq.heappush_max(heap, abs(s1-s2))


        return heap[0] if len(heap) == 1 else 0