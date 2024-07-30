class Solution
{
public:
    int strStr(string haystack, string needle)
    {
        int index = 0;
        for (int i = 0; i < haystack.length(); i++)
        {
            if (haystack[i] == needle[index])
            {
                index++;
            }
            else
            {
                i = i - index; // move back to first matching char
                index = 0;
            }
            if (index == needle.length())
            {
                return i - needle.length() + 1;
            }
        }
        return -1;
    }
};