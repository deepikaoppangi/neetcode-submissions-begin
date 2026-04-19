# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         nums.sort();
#         for i in range(1,len(nums)):
#             if nums[i] == nums[i-1]:
#                 return True;
#         return False;


# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         return len(set(nums)) < len(nums)


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)<1: return False
        mset = set()
        for num in nums:
            if num in mset:
                return True
            mset.add(num)

        return False