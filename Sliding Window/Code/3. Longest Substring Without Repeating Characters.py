'''
Given a string s, find the length of the longest substring without duplicate characters.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        left = 0
        elems = {}

        for right in range(len(s)):
            if s[right] not in elems:
                elems[s[right]] = right
            else:
                while s[left] != s[right]:
                    del elems[s[left]]
                    left += 1
                left += 1

            maxLength = max(right - left + 1, maxLength)
        return maxLength


