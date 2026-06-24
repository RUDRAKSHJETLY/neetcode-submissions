class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for n in nums:
            dict[n]=dict.get(n,0)+1
        ans=[]
        for i in range(k):
            top=max(dict,key=dict.get)
            ans.append(top)
            del dict[top]
        return ans
    