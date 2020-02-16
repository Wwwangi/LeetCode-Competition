class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        squares=[n*n for n in A]
        squares.sort()
        return squares