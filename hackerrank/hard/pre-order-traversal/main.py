class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def preOrder(root):
    node = root
    abc = [root]
    ans = []
    while True:
        if len(abc) == 0:
            break
        if node.left is not None and node.right is not None:
            node = abc.pop()
            ans.append(node.info)
            abc.append(node.right)
            abc.append(node.left)
            node = node.left
        elif node.left is not None:
            node = abc.pop()
            ans.append(node.info)
            abc.append(node.left)
            node = node.left
        elif node.right is not None:
            node = abc.pop()
            ans.append(node.info)
            abc.append(node.right)
            node = node.right
        else:
            node = abc.pop()
            if node.left is not None or node.right is not None:
                abc.append(node)
                continue
            ans.append(node.info)
    print(*ans)


tree = BinarySearchTree()
a = 15
t = int(a)

b = [1, 14, 3, 7, 4, 5, 15, 6, 13, 10, 11, 2, 12, 8, 9]
arr = b

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)
