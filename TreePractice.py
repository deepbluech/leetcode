# coding=utf-8
__author__ = 'samsung'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_tree(cstr):
    global i
    i += 1
    if i >= len(cstr) or cstr[i] == '#':
        root = None
    else:
        root = TreeNode(cstr[i])
        root.left = create_tree(cstr)
        root.right = create_tree(cstr)
    return root


def test():
    return 1, 2


def preorder(root):
    if root is not None:
        print root.val
        preorder(root.left)
        preorder(root.right)


def midorder(root):
    if root is not None:
        midorder(root.left)
        print root.val
        midorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print root.val


def preorder_norec(root):  # 看看会不会改变root的值
    stack = []
    visited = []
    while root is not None:
        print root.val
        visited.append(root)
        stack.append(root)
        root = root.left
    while len(stack) > 0:
        node = stack.pop()
        leftnode = node.left
        while leftnode is not None and leftnode not in visited:
            print leftnode.val
            visited.append(leftnode)
            stack.append(leftnode)
            leftnode = leftnode.left
        rightnode = node.right
        if rightnode != None:
            print rightnode.val
            stack.append(rightnode)
            visited.append(rightnode)

def preorder_norec2(root):
    stack = []
    while root is not None or len(stack) > 0:
        while root is not None:
            print root.val
            stack.append(root)
            root = root.left
        if len(stack) > 0:
            root = (stack.pop()).right

def postorder2(root):
    stack = []
    while root is not None or len(stack) > 0:
        while root is not None:
            stack.append([root, 1])
            root = root.left
        while len(stack) > 0 and stack[-1][1] == 2:
            pair = stack.pop()
            print pair[0].val
        if len(stack) > 0:
            stack[-1][1] = 2
            root = stack[-1][0].right


def inorder(root):
    stack = []
    while root is not None or len(stack) > 0:
        while root is not None:
            stack.append(root)
            root = root.left
        if len(stack) > 0:
            popnode = stack.pop()
            print popnode.val
            root = popnode.right


def levelorder(root):
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        print node.val
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


if __name__ == '__main__':
    create_str = 'ABD#G###CE##F##'
    # 'ABD#G##CE##F##'
    i = -1
    root = create_tree(create_str)
    levelorder(root)
