class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        ans=[]
        from collections import Counter
        tempA=Counter(A.split())
        tempB=Counter(B.split())
        for key in tempA.keys():
            if(tempA[key]==1 and key not in tempB.keys()):
                ans.append(key)
        for key in tempB.keys():
            if(tempB[key]==1 and key not in tempA.keys()):
                ans.append(key)
        return ans