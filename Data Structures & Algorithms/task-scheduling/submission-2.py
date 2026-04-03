class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        

        freq = Counter(tasks)

        heap = []
        cooldown = deque([])
        time = 0

        for i, j in freq.items():
            heapq.heappush(heap, -j)

        while heap or cooldown:
            time += 1
            
            if heap: 
                freq = heapq.heappop(heap)
           
                new_freq = freq + 1 
                available = time + n

                if new_freq < 0:
                    cooldown.append((available, new_freq))

            while cooldown and cooldown[0][0] <= time:
                ready_time, count = cooldown.popleft()
                heapq.heappush(heap, count)   
        
    

        return time