# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s="".join(sorted(s))
#         t="".join(sorted(t))
#         if s==t: 
#             return True
#         else:
#             return False
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        array_cnt=[0]*(26)
        for i in range(0,len(s)):
            array_cnt[ord(s[i])-ord('a')]+=1
            array_cnt[ord(t[i])-ord('a')]-=1

        for i in range(0,len(s)):
            if array_cnt[ord(s[i])-ord('a')] !=0:
                return False

        return True

        