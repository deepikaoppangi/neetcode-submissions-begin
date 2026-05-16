# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         s=""
#         for i in range(0,len(strs)):
#             for j in range(i+1,len(strs)):
#                 if strs[i][i]==strs[j][i]:
#                     s=s+strs[i][i]
#                 else:
#                     break
        
#         return s


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        k = float('inf')
        for i in range(0,len(strs)):
            k = min(k,len(strs[i]))
        for i in range(0,k):
            for j in range(0,len(strs)-1):
                if strs[j][i]!=strs[j+1][i]:
                    return s
            s=s+strs[0][i]
        
        return s