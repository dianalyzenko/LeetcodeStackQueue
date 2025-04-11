class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)

class MyStack(object):

    def __init__(self):
        self.input_queue = Queue()
        self.output_queue = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.input_queue.enqueue(x)
        while not self.output_queue.is_empty():
            self.input_queue.enqueue(self.output_queue.dequeue())
        self.input_queue, self.output_queue = self.output_queue, self.input_queue

    def pop(self):
        """
        :rtype: int
        """
        if self.output_queue.is_empty():
            raise IndexError("Stack is empty")
        return self.output_queue.dequeue()

        

    def top(self):
        """
        :rtype: int
        """
        if self.output_queue.is_empty():
            raise IndexError("Stack is empty")
        top_element = self.output_queue.dequeue()
        self.input_queue.enqueue(top_element)
        while not self.output_queue.is_empty():
            self.input_queue.enqueue(self.output_queue.dequeue())
        self.input_queue, self.output_queue = self.output_queue, self.input_queue
        return top_element

    def empty(self):
        """
        :rtype: bool
        """
        return self.output_queue.is_empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()