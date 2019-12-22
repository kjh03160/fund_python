class Node:
    def __init__(self, key = None, left = None, right = None, num = None):
        self.key = key
        self.num = num
        self.left = left
        self.right = right
        self.num = 0
    # left, right 둘 다 None이면 leaf Node

class Tree:
    def __init__(self, root):
        self.root = root
        self.num = 0

    # 순회
    def preorder(self, v, k = False,  ch = None): # v는 노드
        if k:
            if v != None:
                if v.key == ch:
                    self.num += 1
                self.preorder(v.left, True, ch)    # L
                self.preorder(v.right, True, ch)   # R
        else:
            if v != None:
                print(v.key, end = " ")        # M
                self.preorder(v.left)    # L
                self.preorder(v.right)

    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key, end = " ")
            self.inorder(v.right)

    def postorder(self, v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end = " ")

    def search(self, v, key):
        if v:
            left = self.search(v.left, key)
            right = self.search(v.right, key)
            if v.key == key:
                num = 1
            else: num = 0
            result = left + right + num
            return result
        return 0

    def search2(self, v):
        self.preorder(self.root, k = True, ch = v)
        return self.num


    def number(self, x):
        if x == None:
            return 0
        else:
            left = self.number(x.left)
            right = self.number(x.right)
            result = left + right + 1
            return result

first = Node('A')
second = Node('B')
third = Node('C')
f = Node('D')
fiv = Node('*', first, second)
six = Node('/', third, f)
seven = Node('-', fiv, six)
T1 = Tree(seven)

T1.preorder(T1.root)
print()
T1.inorder(T1.root)
print()
T1.postorder(T1.root)
print()
n1 = Node('A')
n2 = Node('B')
n3 = Node('A')
n4 = Node('D')
n5 = Node('C')
n6 = Node('D', n1, n2)
n7 = Node('C', n3, n4)
n8 = Node('A', n5)
n9 = Node('D')
n10 = Node('B', n6, n7)
n11 = Node('B', n8, n9)
n12 = Node('A', n10, n11)

T2 = Tree(n12)
T2.preorder(n12)
a = input('Input a data : ')
print(T2.search2(a))