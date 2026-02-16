class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def _helperChecker(l, r):
            nonlocal res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r -= 1


        for i in range(len(s)):
            # odd length
            l, r = i, i
            _helperChecker(l, r)

            l, r = i, i+1
            _helperChecker(l, r)

        return res
