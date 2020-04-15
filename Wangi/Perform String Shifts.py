class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        length=0
        for position in shift:
            if(position[0]==0):
                length-=position[1]
            else:
                length+=position[1]
        length=len(s)-length%len(s)
        return s[length:]+s[:length]
        