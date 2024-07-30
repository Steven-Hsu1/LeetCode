class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        int maxLen = 0;
        unordered_set<char> set;
        int left = 0;
        for (int r = 0; r < s.length(); r++)
        {
            while (set.count(s[r]))
            {
                set.erase(s[left]);
                left++;
            }
            set.insert(s[r]);
            maxLen = max(maxLen, r - left + 1);
        }
        return maxLen;
    }
};