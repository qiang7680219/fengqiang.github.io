class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []



    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """

        self.lst.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        #index = self.lst[-1]
        tail = self.lst[-1]
        n = len(self.lst)

        self.lst.remove(tail)

        print('tail=',tail)
        return tail




    def top(self) -> int:
        """
        Get the top element.
        """


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.lst:
            return False
        else:
            return True




# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(3)
obj.push(8)
param_2 = obj.pop()
# param_3 = obj.top()
param_4 = obj.empty()

print('empt=',param_4)