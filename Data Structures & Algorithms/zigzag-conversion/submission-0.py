class Solution:
    def convert(self, s: str, numRows: int) -> str:
        N = len(s)
        res = ""
        # in the numrows = 1 case, return s
        if numRows == 1:
            res += s
            return res
        # in the numrows > 1 case, numDiagonal = numRows - 2
        index = 0
        # first line
        while index < N:
            res += s[index]
            index += numRows + (numRows - 2)
        # zigzag
        numDiagonals = numRows - 2
        for index in range(1, numRows - 1):
            after = 0
            flag = 0
            while index < N and numDiagonals > 0:
                if flag == 0:
                    flag = 1
                    # before diagonal
                    if after == 0:
                        after = index
                        res += s[index]
                    # after diagonal
                    else:
                        index = index + (2 * after)
                        if index < N:
                            res += s[index]
                # we are now doing a diagonal part
                else:
                    flag = 0
                    index = index + (numRows - 1) - (index % (numRows - 1)) + numDiagonals
                    if index < N:
                        res += s[index]
            numDiagonals -= 1
        # last line
        index = numRows - 1
        while index < N:
            res += s[index]
            index += 2 * (numRows - 1)
        return res


            
            

            