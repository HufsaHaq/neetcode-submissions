class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_map = {}
        window = {}

        for i in s1:
            s1_map[i] = 1 + s1_map.get(i,0)
        
        # okay need sliding window approach
        l = 0
        have = 0
        need = len(set(list(s1))) # we only need to know how many unique cahrs there are

        for r in range(len(s2)):
            if s2[r] in s1:
                window[s2[r]] = 1 + window.get(s2[r],0)

                if window.get(s2[r],0) == s1_map.get(s2[r],0):
                    have += 1

            if (r - l + 1) > len(s1): # increase l so the window size is the same size of s1 so we can make sure chars of s1 are next to eacj other in s2
                if s2[l] in s1:
                    if window[s2[l]] == s1_map[s2[l]]: #You should only decrement have if the window previously had that char matched exactly
                        have -= 1
                    window[s2[l]] -= 1

                l+=1

            if have == need and (r - l + 1) == len(s1):
                return True

        return False


        
