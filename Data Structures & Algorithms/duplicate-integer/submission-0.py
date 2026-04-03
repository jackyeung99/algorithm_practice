class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        char_map = set()

        for i in nums:
            if i in char_map:
                return True
            char_map.add(i)

        return False