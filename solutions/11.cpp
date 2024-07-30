class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int n = height.size();
        int left = 0;
        int right = n - 1;
        int maxArea = 0;
        while (left < right)
        {
            // find area
            int minHeight = min(height[left], height[right]);
            int area = minHeight * (right - left);
            maxArea = max(maxArea, area);
            // move pointer to maximize the height
            height[left] > height[right] ? right-- : left++;
        }
        return maxArea;
    }
};