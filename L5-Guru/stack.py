# A stack from scratch
class Stack:
    def __init__(self):
        self.stack_list = []


stack_object = Stack()
# prints the stack
print(len(stack_object.stack_list))


class Stack:
    def __init__(self):
        self.stack_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.__stack_list = []


stack_object = Stack()
print(len(stack_object.stack_list))
