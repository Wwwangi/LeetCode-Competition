class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S=S.replace('-','').upper()
        first=len(S)%K
        S=list(S)
        if(first!=0 and first<len(S)):
            S.insert(first,'-')
            first+=K+1
        else:
            first=K
        while first<len(S):
            S.insert(first,'-')
            first+=K+1
        return ''.join(S)
        
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        arr=[]
        S=S.replace('-','').upper()
        rem=len(S) % K
        if rem != 0:
            arr.append(S[:rem])
        for i in range(rem, len(S), K):
            arr.append(S[i:i+K])
        return '-'.join(arr)