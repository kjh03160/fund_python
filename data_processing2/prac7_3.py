class Stack:
    stack_limit = 100

    def __init__(self):
        self.item = []

    def push(self, value):
        if len(self.item)  == Stack.stack_limit:
            print("Stack OverFlow!")
        else:
            self.item.append(value)
            # print(value, "inserted")

    def pop(self):
        if len(self.item) == 0:
            print("Stack Empty!")
        else:
            val = self.item.pop()
            # print(val, "deleted")
            return val


    def __call__(self):
        return (self.item)

    def __len__(self):
        return len(self.item)


stack = Stack()
string = ''
while True:
    a = input("입력 : ")
    if not a.isalpha():
        break
    stack.push(a)

print("1>>>", stack())
while True:
    if len(stack) == 0:
        break
    string += stack.pop()

print("2>>>", stack())
print("3>>>", string)