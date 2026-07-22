'''

        window_map = {} # this stores the number of occurences wheve seen of the chars in t 
        t_map = {}

        have = 0 # how many conditions we've met 
        need = len(t) # how many conditions we need to meet

        res = [] # will store start index and end index of the substring
        length = len(s) # store length of substring so we know if we've found a smaller one

        l, r = 0,0 #increment r until have = need then increment l until contion is broken have < need the  increment r
'''    
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
                    

            
        