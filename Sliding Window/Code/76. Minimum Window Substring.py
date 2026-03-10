'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        n = len(s)
        m = len(t)

        if n < m:
            return ""

        counts = {}
        for i in t:
            counts[i] = counts.get(i, 0) + 1

        minLen = n + 1
        string = ""
        hashing = {}
        left = 0
        found = False

        for right in range(n):
            if s[right] in counts:
                elem = hashing.get(s[right], 0)
                hashing[s[right]] = elem + 1
                if all(hashing.get(c, 0) >= counts[c] for c in counts):
                    if right - left + 1 <= minLen:
                        minLen = right - left + 1
                        string = s[left:right + 1]

                    while all(hashing.get(c, 0) >= counts[c] for c in counts):
                        if right - left + 1 < minLen:
                            minLen = right - left + 1
                            string = s[left:right + 1]

                        if s[left] in hashing:
                            hashing[s[left]] -= 1
                        left += 1

        return string




