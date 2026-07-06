class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        if digits == "":
            return [] 
            
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def back(i, curr):
            if len(curr) == len(digits):
                res.append("".join(curr[:]))
                return

            for j in range(i, len(digits)):
                for letter in digitToChar[digits[i]]:
                    curr.append(letter)
                    back(j+1, curr)
                    curr.pop()
        back(0, [])
        return res


        