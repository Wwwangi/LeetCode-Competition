class Solution:
    def isValid(self, s: str) -> bool:
        dic={'(':')','[':']','{':'}'}
        stack=[]
        for char in s:
            if(stack and stack[-1] in dic.keys() and char==dic[stack[-1]]):
                stack.pop()
            else:
                stack.append(char)
        if stack:
            return False
        else:
            return True