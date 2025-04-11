class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)

class MyQueue(object):
    def __init__(self):
        self.stack_input = Stack()
        self.stack_output = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_input.push(x)
        
    def pop(self):
        """
        :rtype: int
        """
        if self.stack_output.is_empty():
            while not self.stack_input.is_empty():
                self.stack_output.push(self.stack_input.pop())
        return self.stack_output.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.stack_output.is_empty():
            while not self.stack_input.is_empty():
                self.stack_output.push(self.stack_input.pop())
        return self.stack_output.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack_input.is_empty() and self.stack_output.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
