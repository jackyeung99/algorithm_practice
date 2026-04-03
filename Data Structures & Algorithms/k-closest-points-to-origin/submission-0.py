import math 
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        heap = []
        for i, j in points:

            dis = math.sqrt((i)**2 + (j)**2)
            heapq.heappush(heap, [dis, (i, j)])

        res = []
        for i in range(k): 
            dis, (i,j) = heapq.heappop(heap)
            res.append([i,j])

        return res