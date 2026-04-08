class MedianFinder:

    def __init__(self):
        
        # min heap 
        self.high = []
        self.n_high = 0
        
        # max heap 
        self.low = []
        self.n_low = 0

    def addNum(self, num: int) -> None:
        if self.high and num > self.high[0]:
            heapq.heappush(self.high, num)
            self.n_high += 1
        else:
            heapq.heappush_max(self.low, num)
            self.n_low += 1

        if self.n_high > self.n_low + 1:
            val = heapq.heappop(self.high)
            heapq.heappush_max(self.low, val)
            self.n_high -= 1
            self.n_low += 1

        elif self.n_low > self.n_high + 1:
            val = heapq.heappop_max(self.low)
            heapq.heappush(self.high, val)
            self.n_low -= 1
            self.n_high += 1

    
    def findMedian(self) -> float:
        # print(self.low, self.high)
        # print(self.n_low, self.n_high)
        if self.n_low == 0 and self.n_low == self.n_high:
            return None 


        if self.n_low == self.n_high:
            return (self.high[0] + self.low[0]) / 2 
        elif self.n_low > self.n_high:
            return self.low[0]
        else:
            return self.high[0]

