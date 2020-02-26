class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dic={'qwertyuiopQWERTYUIOP':0,'asdfghjklASDFGHJKL':0,'zxcvbnmZXCVBNM':0}
        res=[]
        for word in words:
            for char in word:
                for item in dic.keys():
                    if(char in item):
                        dic[item]+=1
                    if(dic[item]==len(word)):
                        res.append(word)
            for item in dic.keys():
                dic[item]=0
        return res

#用set做
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = [
            {'q','w','e','r','t','y','u','i','o','p'},
            {'a','s','d','f','g','h','j','k','l'},
            {'z','x','c','v','b','n','m'}
        ]
        answer = []
        for word in words:
            letters = set(word.lower())
            for row in keyboard:
                if letters.issubset(row):
                    answer.append(word)
        return answer