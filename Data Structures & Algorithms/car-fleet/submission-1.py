class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        iterator = sorted(zip(position, speed), key =lambda x:x[0], reverse =True)
        
        groups = []

        for pos, sp in iterator: 



            speed = (target - pos) / sp

            groups.append(speed)

            if len(groups) >= 2 and groups[-1] <= groups[-2]: 
                groups.pop()

        return len(groups)