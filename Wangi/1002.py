class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        from collections import Counter
        res = Counter(A.pop())
        while A:
            word = A.pop()
            res = res & Counter(word)
        return res.elements()