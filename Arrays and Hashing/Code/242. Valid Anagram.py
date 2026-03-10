class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        elems1 = {}
        elems2 = {}

        for i in range(len(s)):
            elems1[s[i]] = elems1.get(s[i], 0) + 1
            elems2[t[i]] = elems2.get(t[i], 0) + 1
        return elems1 == elems2