class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_modified=[]
        t_modified=[]
        for char in S:
            if(char=='#' and s_modified):
                s_modified.pop()
            elif(char!="#"):
                s_modified.append(char)
        for char in T:
            if(char=='#' and t_modified):
                t_modified.pop()
            elif(char!="#"):
                t_modified.append(char)
        return s_modified==t_modified
        
            