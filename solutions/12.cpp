class Solution
{
public:
    string intToRoman(int num)
    {
        string ans = "";
        vector<pair<int, string>> map = {{1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"}, {100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"}, {10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}};
        for (int i = 0; i < map.size(); i++)
        {
            while (num >= map[i].first)
            {
                ans += map[i].second;
                num -= map[i].first;
            }
        }
        return ans;
    }
};