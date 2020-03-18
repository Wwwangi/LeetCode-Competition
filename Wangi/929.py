class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        temp={}
        for email in emails:
            local=email.split('@')[0].split('+')[0]
            domain=email.split('@')[1]
            local=local.replace('.','')
            if(local not in temp.keys()):
                temp[local]=[domain]
            else:
                if(domain not in temp[local]):
                    temp[local].append(domain)
        res=0
        for key in temp.keys():
            res+=len(temp[key])
        return res

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res=set()
        for email in emails:
            local=email.split('@')[0].split('+')[0]
            domain=email.split('@')[1]
            local=local.replace('.','')
            res.add(local+'@'+domain)
        return len(res)