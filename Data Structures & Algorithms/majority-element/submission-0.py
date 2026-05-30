class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k=0
        ans=nums[0]
        mp={}   # unordered map
        for i in range(0,len(nums)):
            mp[nums[i]]=mp.get(nums[i],0)+1
            if mp[nums[i]] > k:
                k=mp[nums[i]]
                ans=nums[i]
        return ans

        