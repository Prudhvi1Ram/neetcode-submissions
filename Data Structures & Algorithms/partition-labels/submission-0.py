class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex={}
        for i,j in enumerate(s):
            lastindex[j]=i
        res=[]
        start,end=0,0
        for i,j in enumerate(s):
            start+=1
            end=max(end,lastindex[j])
            if i == end:
                res.append(start)
                start=0
        return res