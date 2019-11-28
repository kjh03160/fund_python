class Node:
    def __init__(self, data, left = None, right = None):
        self.__data = data
        self.__left = left
        self.__right = right

    def get_right(self):
        return self.__right

    def get_left(self):
        return self.__left

    def get_data(self):
        return self.__data

class Tree:
    def __init__(self, root):
        self.root = root

n1 = Node('D')
n2 = Node('E')
n3 = Node('F')
n4 = Node('G')
n5 = Node('B', n1, n2)
n6 = Node('C', n3, n4)
n7 = Node('A', n5, n6)

T1 = Tree(n7)
print(T1.root.get_data())
print(n5.get_data())
print(n5.get_right().get_data())
