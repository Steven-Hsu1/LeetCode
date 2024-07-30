class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        string prefix = "";
        string common = strs[0];
        for (int i = 1; i < strs.size(); i++)
        {
            prefix = "";
            string next = strs[i];
            int index = 0;
            while (index < common.length() && index < next.length())
            {
                if (common[index] != next[index])
                {
                    break;
                }
                prefix += common[index];
                index++;
            }
            common = prefix;
        }
        return common;
    }
};