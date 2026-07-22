class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        substring = []
        count = 0
        results = [0]
        for i in range(len(s)):
            substring.append(s[i])
            while s[i] in chars:
                valuetoremove = substring.pop(0)
                chars.remove(valuetoremove)
            chars.add(s[i])
            results.append(len(substring))
        return max(results)