from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q2.append(x)
        for i in range(len(self.q1)):
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q1.popleft()
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q1[0]
        
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.q1:
            return False
        return True
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()