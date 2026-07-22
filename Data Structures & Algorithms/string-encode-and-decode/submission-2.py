class Solution:

    def encode(self, strs: List[str]) -> str:
        returnstring = ""
        separator=[]
        for i in strs:
            separator.append('Á'  + str(len(i))+ 'Á' )
        for i in range(len(strs)):
            returnstring = returnstring + separator[i] + strs[i]

        print(returnstring)
        return returnstring


    def decode(self, s: str) -> List[str]:
        indexes = []
        returnlist =[]
        values = []
        seperator = [i for i, letter in enumerate(s) if letter == 'Á' ]
        seperator.append(len(s))
        
        for i in range(len(seperator)-1):
            values.append(s[seperator[i]+1:seperator[i+1]])

        for i in values:
            i = i.replace('Á','')
            if i.isdigit():
                values.remove(i)
        return values