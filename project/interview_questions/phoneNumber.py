#https://leetcode.com/problems/letter-combinations-of-a-phone-number/

def letterCombinations(digits: str):
    DIGIT_MAPPING = {
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz"
}
    digitList = []
    firstValue = list((DIGIT_MAPPING[digits[0]]))
    secondValue = list((DIGIT_MAPPING[digits[1]]))
    for firstLetter in firstValue:
        for secondLetter in secondValue:
            letterCombo = firstLetter + secondLetter
            digitList.append(letterCombo)
    return digitList

# Nigel's Answer
DIGIT_MAPPING = {
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz"
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return backtrack(0, "", digits)
        
def backtrack(pos, cur, digits) -> List[str]:
    if pos == len(digits):
        return [cur] if cur else []
    
    result = []
    for letter in DIGIT_MAPPING[digits[pos]]:
        result.extend(backtrack(pos + 1, cur + letter, digits))
    
    return result


letterCombinations('23')