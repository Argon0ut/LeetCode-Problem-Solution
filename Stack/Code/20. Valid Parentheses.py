'''

Topics
premium lock icon
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        check = '[{('

        if n % 2 == 1 or s[0] not in check:
            return False

        stack1 = []
        stack2 = []
        stack3 = []

        for i in range(n):

            if s[i] in check:
                if s[i] == '(':
                    stack1.append(i)
                elif s[i] == '[':
                    stack2.append(i)
                else:
                    stack3.append(i)

            else:
                if s[i] == ')':
                    if not stack1 or (i - stack1[-1] - 1) % 2 == 1 or s[i - 1] in '[{':
                        return False
                    else:
                        stack1.pop()

                elif s[i] == '}':
                    if not stack3 or (i - stack3[-1] - 1) % 2 == 1 or s[i - 1] in '([':
                        return False
                    else:
                        stack3.pop()

                else:
                    if not stack2 or (i - stack2[-1] - 1) % 2 == 1 or s[i - 1] in '({':
                        return False
                    else:
                        stack2.pop()

        return len(stack1) == len(stack2) == len(stack3) == 0
