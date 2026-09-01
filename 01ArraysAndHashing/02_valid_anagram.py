# Valid Anagram
# Easy
# Topics
# Company Tags
# Hints
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false
# Constraints:

# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.

class Solution:
    def valid_anagram(self,s:str, t:str):
        if len(s) != len(t):
            return False
        countS, countT = {},{}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        for c in countS:
            if countS.get(c,0) != countT.get(c,0):
                return False
        return True

soln = Solution()
print(soln.valid_anagram( s = "raceccar", t = "carrace"))