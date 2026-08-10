class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_1 = 0
        for i in s:
            if i == '1':
                count_1 += 1

        return '1' * (count_1 - 1) + '0' * (len(s) - count_1) + '1'

        