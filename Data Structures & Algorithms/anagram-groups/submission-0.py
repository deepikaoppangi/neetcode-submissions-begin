class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for i in range(len(strs)):
            word = strs[i]
            key = "".join(sorted(word))

            if key not in mp:
                mp[key] = []
                
            mp[key].append(word)

        return list(mp.values())







        
