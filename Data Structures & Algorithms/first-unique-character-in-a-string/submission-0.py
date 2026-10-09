
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_freq = defaultdict(int)

        for i in s:
            char_freq[i] = 1 + char_freq.get(i, 0)

        for i in range(len(s)):
            if char_freq[s[i]] == 1:
                return i   

        return -1