// class Solution {
// public:
//     bool hasDuplicate(vector<int>& nums) {
//         sort(nums.begin(),nums.end());
//         for(int i=1;i<nums.size();i++){
//             if(nums[i]==nums[i-1]){
//                 return true;
//             }
//         }
//         return false;
//     }
// };


class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        if(nums.size()<=1){
            return false;
        }
        unordered_set<int> mset;
        // mset.reserve(nums.size()*2);
        for(int i=0;i<nums.size();i++){
            if( mset.find(nums[i]) != mset.end() ){
                return true;
            }
            mset.insert(nums[i]);
        }
        return false;
    }
};