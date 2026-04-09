class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        out = []
        def bt(res = [], left=n, right=n):

            

            if left == right and left == 0:
                out.append("".join(res))
                return


            if left == right:
                res.append('(')
                bt(res, left-1, right)
                res.pop()
            else:

                if left > 0: 
                    res.append('(')
                    bt(res, left-1, right)
                    res.pop()
                if right > 0:
                    res.append(')')
                    bt(res, left, right-1)
                    res.pop()


        bt()

        print(out)
        return out








