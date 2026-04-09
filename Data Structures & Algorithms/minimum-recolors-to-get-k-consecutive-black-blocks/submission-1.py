class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        


        l = 0
        min_ops = float('inf')
        operations = 0 

        for idx, i in enumerate(blocks):  
            
            if i == 'W':
                operations += 1
            
            while (idx-l+1) > k :
                
                # print('  ', l)
                if blocks[l] == 'W':
                    operations -= 1

                l += 1

            if (idx-l+1) == k:
                min_ops = min(min_ops, operations)


        return min_ops

