class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        for i in range(len(digits)):
            num+=digits[len(digits)-1-i] * (10 **i)
        num+=1
        after=[]
        while num>=1:
            after.append(num%10)
            num=int(num/10)
        return list(reversed(after))

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        for i in range(len(digits)):
            num+=digits[len(digits)-1-i] * (10 **i)
        num+=1
        return list(str(num))