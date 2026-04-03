class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        candidates.sort()

        out = []
        def bfs(idx , res=[], cur_sum=0):
            if cur_sum == target:
                out.append(res.copy())
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue

                if cur_sum + candidates[i] > target:
                    break
            

                res.append(candidates[i])
                bfs(i+1, res, cur_sum + candidates[i])
                res.pop()




        bfs(0)

        return out