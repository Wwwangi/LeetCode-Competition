class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=collections.defaultdict(list)
        for word in strs:
            dic[tuple(sorted(word))].append(word)
        return dic.values()

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for word in strs:
            temp=sorted([x for x in word])
            if tuple(temp) not in dic.keys():
                dic[tuple(temp)]=[word]
            else:
                dic[tuple(temp)].append(word)
        return dic.values()