class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub=nums[0]
        curr=0
        for i in nums:
            if curr<0:
                curr=0
            curr+=i
            maxsub=max(maxsub,curr)
        return maxsub