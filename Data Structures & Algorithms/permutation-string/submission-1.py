class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # idea is that we keep track of the matches in the window size of s1 ie if s1 == "abc", keep window size of 3
        # we have to populate a matches either map or array to see which characters match in that particular window
        # if all 26 characters match, then we are good. if we haven't found a complete match, shift the window
        # over by 1 ie update the right character match and left character match
        if len(s1) > len(s2):
            return False
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            l += 1
        return matches == 26