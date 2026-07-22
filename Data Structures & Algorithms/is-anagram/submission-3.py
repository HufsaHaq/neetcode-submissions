class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for i in s:
            s_map[i] = 1 + s_map.get(i,0)
        for i in t:
            t_map[i] = 1 + t_map.get(i,0)  
        if s_map != t_map : return False
        return True         
        