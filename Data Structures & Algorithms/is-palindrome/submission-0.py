import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for i in string.punctuation:
            s= s.replace(i,'')
        s = s.replace(' ','')
        print(s)
        print(s[::-1])
        return True if (s == s[::-1]) else False
        