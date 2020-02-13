#用118的方法
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result=[]
        numRows=rowIndex+1
        for i in range(numRows):
            temp=[]
            if(i==0):
                result.append([1])
            elif(i==1):
                result.append([1,1])
            else:
                temp.append(1)
                for j in range(1,i+1):
                    try:
                        temp.append(result[i-1][j-1]+result[i-1][j])
                    except:
                        temp.append(1)
                result.append(temp)
        return result[-1]

#组合数解答，后面一项是前一项乘上n-r+1/r
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result=[1]
        for i in range(1,rowIndex+1):
            result.append(int(result[-1]*(rowIndex-i+1)/i))
        return result