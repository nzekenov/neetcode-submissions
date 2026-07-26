class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s) + 1):
            for j in range(i, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:                    
                    if len(s[i:j]) > len(longest):
                        longest = s[i:j]
        return longest