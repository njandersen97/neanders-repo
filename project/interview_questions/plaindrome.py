#https://leetcode.com/problems/valid-palindrome/
# My Solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        inputStr = ""
        for char in s:
            if char.isalnum():
                inputStr += char.lower()
        return inputStr == inputStr[::-1]

# Better Solution
    def isPalindromeV2(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        while L < R:
            while L < R and not s[L].isalnum():
                L += 1
            while R > L and not s[R].isalnum():
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L, R = L + 1, R - 1
        return True
