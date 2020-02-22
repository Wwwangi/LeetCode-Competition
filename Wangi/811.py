#我的写法
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic={}
        for url in cpdomains:
            temp=url.split(' ',1)
            count=int(temp[0])
            string=temp[1]
            dic[string]=dic.get(string,0)+count
            while('.' in string):
                subdomain=string.split('.',1)[1]
                dic[subdomain]=dic.get(subdomain,0)+count
                string=subdomain
        res=[]
        for item in dic.keys():
            res.append(str(dic[item])+' '+item)
        return res

#有些写法值得借鉴
class Solution(object):
    def subdomainVisits(self, cpdomains):
        ans = collections.Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in xrange(len(frags)):
                ans[".".join(frags[i:])] += count

        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]