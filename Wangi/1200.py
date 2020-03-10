class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff=arr[1]-arr[0]
        res=[]
        for i in range(len(arr)-1):
            if(arr[i+1]-arr[i]<diff):
                diff=arr[i+1]-arr[i]
        for i in range(len(arr)-1):
            if(arr[i+1]-arr[i]==diff):
                res.append([arr[i],arr[i+1]])
        return res

class Solution:
    def minimumAbsDifference(self, a):
        a.sort()

        min_diff = a[1] - a[0] # large number > 2 * 10**6 (maximum possible difference)
        res = []

        for i in range(1, len(a)):
            diff = a[i] - a[i - 1]
            if diff < min_diff:
                min_diff = diff
                res.clear()

            if diff == min_diff:
                res.append([a[i - 1], a[i]])

        return res

#比较慢
from collections import defaultdict

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr = sorted(arr)
        
        m = defaultdict(list)
        for i in range(len(arr)-1):
            m[arr[i+1] - arr[i]] += [(arr[i], arr[i+1])]
        
        return m[min(m.keys())]