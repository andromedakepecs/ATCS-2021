"""
Andromeda Kepecs
ATCS 2021-2022
Binary Tree

Python program to for binary tree insertion and traversals
"""
from bst_node import Node

'''
A function that returns a string of the inorder 
traversal of a binary tree. 
Each node on the tree should be followed by a '-'.
Ex. "1-2-3-4-5-"
'''
def getInorder(root):
    if root:
        return getInorder(root.left) + str(root.val) + '-' + getInorder(root.right)
    return ''

'''
A function that returns a string of the postorder 
traversal of a binary tree. 
Each node on the tree should be followed by a '-'.
Ex. "1-2-3-4-5-"
'''
# A function to do postorder tree traversal
def getPostorder(root):
    if root:
        return getPostorder(root.left) + getPostorder(root.right) + str(root.val) + '-'
    return ''


'''
A function that returns a string of the preorder 
traversal of a binary tree. 
Each node on the tree should be followed by a '-'.
Ex. "1-2-3-4-5-"
'''
def getPreorder(root):
    if root:
        return str(root.val) + '-' + getPreorder(root.left) + getPreorder(root.right)
    return ''


'''
A function that inserts a Node with the value
key in the proper position of the BST with the
provided root. The function will return the 
original root with no change if the key already
exists in the tree.
'''
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


'''
Challenge: A function determines if a binary tree 
is a valid binary search tree
'''
def isBST(root):
    if root == None:
        return True
    if root.left != None and root.left.val > root.val:
        return False
    if root.right != None and root.right.val < root.val:
        return False
    if not isBST(root.left) or not isBST(root.right):
        return False

    return True


# Test code
def main():
    # Tree to help you test your code
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(9)

    # Preorder test
    print("Preorder traversal of binary tree is")
    print(getPreorder(root))

    # Inorder test
    print("\nInorder traversal of binary tree is")
    print(getInorder(root))

    # Postorder test
    print("\nPostorder traversal of binary tree is")
    print(getPostorder(root))

    # Insertion test
    root = insert(root, 8)
    print("\nInorder traversal of binary tree with 8 inserted is")
    print(getInorder(root))

    # Is BST tree test True
    print(isBST(root))

    bad_tree = Node(10)
    bad_tree.left = Node(15)
    bad_tree.right = Node(16)
    root.left.left = Node(3)
    root.left.right = Node(9)
    print(isBST(bad_tree))

if __name__ == '__main__':
    main()