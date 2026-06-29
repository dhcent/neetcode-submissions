#include <vector>
#include <unordered_map>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> sol;
        unordered_map<int, int> seen;
        for(int i = 0; i < nums.size(); i++) {
            if(seen.contains(target - nums[i])) {
                sol.push_back(seen[target - nums[i]]);
                sol.push_back(i);
                break;
            }
            else {
                seen[nums[i]] = i;
            }
        }
        return sol;
    }
};
