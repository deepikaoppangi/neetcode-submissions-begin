class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(0,len(nums)):
            if nums[i]!=val:
                k=k+1 
                if k-1!=i:
                    nums[k-1]=nums[i]
        return k

        