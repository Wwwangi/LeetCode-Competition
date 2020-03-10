class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res=0
        for i in range(len(points)-1):
            l1=points[i][0]
            r1=points[i][1]
            l2=points[i+1][0]
            r2=points[i+1][1]
            res+=max(abs(l2-l1),abs(r2-r1))
        return res
            