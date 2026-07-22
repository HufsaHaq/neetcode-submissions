class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {} # char:number of occurances
        res = 0 # longest substring we can make with k replacements
        
        l = 0 # left pointer which we will increase
        for r in range(len(s)):
            hash_map[s[r]] = 1 + hash_map.get(s[r], 0) #update hashmap since we have looped so r pointing at new char
            while (r - l + 1) - max(hash_map.values()) > k: # while the window is INVALID
                hash_map[s[l]] = -1 + hash_map.get(s[l] , 0)
                l += 1
            res = max(res, r-l + 1) # update result - r-l +1 is size of window

        return res
            
