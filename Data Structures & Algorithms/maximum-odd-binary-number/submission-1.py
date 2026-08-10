class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        if len(s) ==1:
            return s
        hashset = {}
        returnstring = ""
        for i in s:
            hashset[i] = 1 + hashset.get(i,0)

        returnstring = '1'*(hashset.get('1',0)-1) + '0'*(hashset.get('0',0)) + '1'
        
        return returnstring
        