class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        



        tc = [0 for x in range(len(cost))]  

        tc[0] = cost[0]
        tc[1] = cost[1]


        for i in range(2, len(cost)): 
            tc[i] = min(tc[i-1], tc[i-2]) + cost[i]


        print(tc)
        return min(tc[-1], tc[-2])