class MinStack:

    def __init__(self):
        self.stack = []
        self.aux = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        val = min(val, self.aux[-1] if self.aux else val)
        self.aux.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.aux.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.aux[-1]
