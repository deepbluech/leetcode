__author__ = 'samsung'
lastVisited = None

def flatten(root):
    if root is None:
        return 0

    global lastVisited
    if lastVisited:
        lastVisited.left = None
        lastVisited.right = root

    lastVisited = root
    right = root.right
    flatten(root.left)
    flatten(right)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)

flatten(root)
while root:
    print root.val
    root = root.right