class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # create hash map where char is key and number of occurances is value - do this for both words then compare hashmaps
        s_map = {}
        t_map = {}

        for i in s:
            if i in s_map.keys():
                s_map[i] += 1
            else:
                s_map[i] = 1

        for i in t:
            if i in t_map.keys():
                t_map[i] += 1
            else:
                t_map[i] = 1

        for i in s_map.keys():
            if i not in t_map.keys():
                return False
            elif s_map[i] == t_map[i]:
                continue
            else:
                return False

        return True