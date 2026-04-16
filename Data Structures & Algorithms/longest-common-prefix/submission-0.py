class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common = []

        min_len = float('inf')
        for i in strs:
            min_len = min(min_len, len(i))


        for i in range(min_len):
            val = strs[0][i]
            for word in range(1, len(strs)):
                if not strs[word][i] == val:
                    return ''.join(common)

            common.append(val)

    
        return ''.join(common)