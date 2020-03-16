#有点问题
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res1=0
        res2=0
        length1=len(text1)
        length2=len(text2)
        matrix=[[0 for i in range(length2)] for j in range(length1)]
        for i in range(length1):
            for j in range(length2):
                if(text1[i]==text2[j]):
                    matrix[i][j]=1
        print(matrix)
        position=-1
        for i in range(length2):
            for j in range(position+1,length1):
                if matrix[j][i]==1:
                    position=j
                    res1+=1
        position=-1
        for i in range(length1):
            for j in range(position+1,length2):
                if matrix[i][j]==1:
                    position=j
                    res2+=1            
                
        return max(res1,res2)