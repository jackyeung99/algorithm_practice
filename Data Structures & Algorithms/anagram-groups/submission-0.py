from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        


        anagram_map = defaultdict(list)
        for i in strs:
            anagram_map[''.join(sorted(i))].append(i)



        return [v for k,v in anagram_map.items()]

