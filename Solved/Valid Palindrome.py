from typing import List


class Solution:
    def validPalindrome(self, s: str) -> bool:
        ans = ""
        for i in range(len(s)):
            if s[i] in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
                ans += (s[i]).lower()

        left, right = 0, len(ans)-1
        while left < right:
            if ans[left] != ans[right]:
                return False
            left += 1
            right -= 1

        return True

s = " "
ans = Solution().validPalindrome(s)
print(ans)

