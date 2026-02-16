class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        #Bottom-Up
        dp = {len(s) : 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

            if i + 1 < len(s) and 0 < int(s[i] + s[i+1]) < 27:
                dp[i] += dp[i+2]

        return dp[0]


        #Top-Down

        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0

            res = dfs(i + 1)

            if i + 1 < len(s) and 0 < int(s[i] + s[i + 1]) < 27:
                res += dfs(i + 2)

            dp[i] = res
            return res

        return dfs(0)

