class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        freq=[[] for i in range(len(nums)+1)]
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        for i,j in d.items():
            freq[j].append(i)
        
        res=[]
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
      


        