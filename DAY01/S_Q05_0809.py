class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            if (len(s) - i) < len(longest):
                break
            for j in range(len(s)-i):
                subS = s[i:j+i+1]
                #print(subS)
                revS = subS[::-1]
                #print(revS)
                if (subS == revS) and (len(subS)>len(longest)):
                    longest = subS
        return longest
    
    #can be improved
    #Runtime: 4876 ms, faster than 27.11% of Python3 online submissions for Longest Palindromic Substring.
    #Memory Usage: 13.9 MB, less than 22.69% of Python3 online submissions for Longest Palindromic Substring.
