class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        map<int, int> myMap;
        vector<int> ans;
        for (int i = 0; i < nums.size(); i++)
        {
            myMap[nums[i]] = i;
        }
        for (int i = 0; i < nums.size(); i++)
        {
            int second = target - nums[i];
            if (myMap.contains(second) && myMap.at(second) != i)
            {
                ans = {i, myMap.at(second)};
                return ans;
            }
        }
        return ans;
    }
};