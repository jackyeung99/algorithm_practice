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
                    cooldown.append((new_freq, available))

            else: 
                time = cooldown[0][1]

            if cooldown and cooldown[0][1] == time:
                count, ready_time = cooldown.popleft()
                heapq.heappush(heap, count)   
            
    

        return time