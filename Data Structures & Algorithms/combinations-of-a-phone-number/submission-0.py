class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letter = {2: ["a", "b", "c"],
                           3: ["d", "e", "f"],
                           4: ["g", "h", "i"],
                           5: ["j", "k", "l"],
                           6: ["m", "n", "o"],
                           7: ["p", "q", "r", "s"],
                           8: ["t", "u", "v"],
                           9: ["w", "x", "y", "z"]
                           }
        res = []
        def backtrack(index, ans):
            if index == len(digits):
                res.append(ans)
                return
            for c in digit_to_letter[int(digits[index])]:
                backtrack(index + 1, ans + c)
        if digits:   
            backtrack(0, "")
        return res
        


