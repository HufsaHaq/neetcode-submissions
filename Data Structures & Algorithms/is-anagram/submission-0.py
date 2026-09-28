from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)

        for i in s:
            s_map[i] = 1 + s_map.get(i,0)
        for i in t:
            t_map[i] = 1 + t_map.get(i,0)

        if t_map == s_map:
            return True
        return False
        
        