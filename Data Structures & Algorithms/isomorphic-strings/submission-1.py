class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_to_t = {}
        mapping_t_to_s = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            if a in mapping_s_to_t and mapping_s_to_t[a] != b:
                return False
            else:
                mapping_s_to_t[a] = b

            if b in mapping_t_to_s and mapping_t_to_s[b] != a:
                return False
            else:
                mapping_t_to_s[b] = a

        return True