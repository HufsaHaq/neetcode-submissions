class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp_s = list(s)
        temp_t = list(t)
        temp_s.sort()
        temp_t.sort()
        return temp_s == temp_t
        