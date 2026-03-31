class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size()!=t.size()){
            return false;
        }
        int n = s.size();
        unordered_map<char , int> s1;
        unordered_map<char , int> t1;
        for(int i=0;i<n;i++){
            s1[s[i]]++;
            t1[t[i]]++;
        }
        for(int i=0;i<n;i++){
            char x = s[i];
            if(s1[x] != t1[x]){
                return false;
            }
        }
        return true;

    }
};

