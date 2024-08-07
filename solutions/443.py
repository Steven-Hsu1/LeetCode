class Solution:
    def compress(self, chars: List[str]) -> int:
        compressedStr = ""
        l = 0
        count = 0
        for r in range(len(chars)):
            if chars[l] == chars[r] and count < 1:
                compressedStr += chars[r]
            if chars[l] != chars[r]:
                if count > 1:
                    compressedStr += (str(count) + chars[r])
                else:
                    compressedStr += chars[r]
                count = 0
                l = r
            if r == len(chars) - 1:
                if chars[l] == chars[r] and count + 1 > 1:
                    compressedStr += str(count + 1)
                break
            count += 1
        for i in range(len(compressedStr)):
            chars[i] = compressedStr[i]
        return len(compressedStr)

            