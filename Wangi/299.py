class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s={}
        g={}
        for char in secret:
            s[char]=s.get(char,0)+1
        for char in guess:
            g[char]=g.get(char,0)+1     
        total=0
        for i in g.keys():
            if(i in s.keys()):
                total+=min(g[i],s[i])
        
        bull=0
        for i in range(len(secret)):
            if(secret[i]==guess[i]):
                bull+=1
        cow=total-bull
        return str(bull)+'A'+str(cow)+'B'