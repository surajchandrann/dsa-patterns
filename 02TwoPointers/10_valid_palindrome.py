# Valid Palindrome
# Easy
# Topics
# Company Tags
# Hints
# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# Example 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:

# Input: s = "tab a cat"

# Output: false
# Explanation: "tabacat" is not a palindrome.

# Constraints:

# 1 <= s.length <= 1000
# s is made up of only printable ASCII characters.


class Solution:
    def valid_palindrome_1(self,s:str)-> bool:
        new_str = ""

        for c in s:
            if c.isalnum():
                new_str+=c.lower()
        return new_str == new_str[::-1]

    def valid_palindrome_2(self,s:str)-> bool:
        l,r = 0, len(s)-1
        while l < r:
            while l < r and not self.is_alpha_numeric(s[l]):
                l+=1
            while l < r and not self.is_alpha_numeric(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r-1

        return True


    def is_alpha_numeric(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z')or
                ord('0') <= ord(c) <= ord('9'))


soln = Solution()
print(soln.valid_palindrome_1(s = "Was it a car or a cat I saw?"))
print(soln.valid_palindrome_2( s = "Was it a car or a cat I saw?"))