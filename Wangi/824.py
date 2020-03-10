class Solution:
    def toGoatLatin(self, S: str) -> str:
        words=S.split()
        vowel=['a','e','i','o','u','A','E','I','O','U']
        count=0
        res=''
        for word in words:
            count+=1
            if(word[0] in vowel):
                word+='ma'
            else:
                word+=word[0]
                word=word[1:]
                word+='ma'
            for n in range(count):
                word+='a'
            res+=word
            if(count!=len(words)):
                res+=' '
        return res