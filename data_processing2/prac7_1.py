class Stack:
    stack_limit = 3

    def __init__(self):
        self.item = []

    def push(self, value):
        if len(self.item)  == Stack.stack_limit:
            print("Stack OverFlow!")
        else:
            self.item.append(value)
            print(value, "inserted")

    def pop(self):
        if len(self.item) == 0:
            print("Stack Empty!")
        else:
            val = self.item.pop()
            print(val, "deleted")
            return val


    def __call__(self):
        print(self.item)

    def __len__(self):
        return len(self.item)

# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(3)
# s()
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# s()