class Solution:
    def isPalindrome(self, s: str) -> bool:
        def _helper(elem):
            return (
                    ord('A') <= ord(elem) <= ord('Z') or
                    ord('a') <= ord(elem) <= ord('z') or
                    ord('0') <= ord(elem) <= ord('9')
            )

        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not _helper(s[l]):
                l += 1
            while l < r and not _helper(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True