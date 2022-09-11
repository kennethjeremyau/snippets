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

def preorder(node):
    stack = []
    stack.append(node)
    while len(stack) > 0:
        n = stack.pop()
        print(n.data)
        if n.right:
            stack.append(n.right)
        if n.left:
            stack.append(n.left)

preorder(root)
