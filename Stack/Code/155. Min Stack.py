'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
'''

class MinStack:
    def __init__(self):
        self.stack = []
        self.minElements = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minElements) > 0:
            if val <= self.minElements[-1]:
                self.minElements.append(val)
        else:
            self.minElements.append(val)

    def pop(self) -> None:
        r = self.stack.pop()
        if self.minElements[-1] == r:
            self.minElements.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minElements[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

