#用append做的很慢，memory占用也很高
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[]
        if(numRows==0):
            return []
        elif(numRows==1):
            return [[1]]
        elif(numRows==2):
            return [[1],[1,1]]
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
        return result

#不用append
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[[1]* n for n in range(1,numRows+1)]
        if(numRows>=3):
            for i in range(3,numRows+1):
                for j in range(i-2):
                    result[i-1][j+1]=result[i-2][j+1]+result[i-2][j]
        return result
