#greedy
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftbound=0
        rightbound=0
        for char in s:
            if char=='(':
                leftbound+=1
                rightbound+=1
            elif char==')':
                leftbound-=1
                rightbound-=1
            else:
                leftbound-=1
                rightbound+=1
            if rightbound<0:
                return False
            leftbound=max(leftbound,0)
        return leftbound==0
                

#过了55/58个case
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        for char in s:
            print(stack)
            if char=='(':
                stack.append(char)
            elif char==')':
                if stack:
                    temp=stack.pop()
                    if temp=="(":
                        continue
                    elif temp=='*':
                        if stack and stack[-1]=='(':
                            stack.pop()
                            stack.append('*')
                        else:
                            continue
                    else:
                        return False
                else:
                    return False
            else:
                if stack and stack[-1]=='(':
                    stack.append('*')
        print(stack)
        
        count1=0
        count2=0
        for i in range(len(stack)):
            if stack[i]=='(':
                count1+=1
            elif count1!=0 and stack[i]=='*':
                count2+=1
            if count1==count2:
                count1=0
                count2=0
        if count1!=0:
            return False
        return True