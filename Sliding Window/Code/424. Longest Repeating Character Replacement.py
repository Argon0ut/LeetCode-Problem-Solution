'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        maxCount = 0
        maxLength = 0
        left = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            maxCount = max(maxCount, counts[s[right]])

            while (right - left + 1) - maxCount > k:
                counts[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)
        return maxLength
    