#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

def visit(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return node.data
    return visit(node.left) + visit(node.right)

print(visit(root))
