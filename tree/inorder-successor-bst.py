'''

Given the root of a binary search tree (BST) and a tree node x, find the inorder successor of x in the BST. An inorder successor of a tree node is the next node in the inorder traversal of the tree.

For example, consider the following tree:

		  15
		/	 \
	   /	  \
	  /		   \
	 10		   20
	/  \	  /  \
   /	\	 /	  \
  8		12	16	  25

Input: Node 10
Output: Node 12

Input: Node 12
Output: Node 15

• If the node does not lie in the BST, return the next greater node (if any) present in the BST.

Input: Node 5
Output: Node 8

• If the node does not lie in the BST and the next greater node also does not exist, the solution should return None.

Input: Node 30
Output: None

'''


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data  # data field
        self.left = left  # pointer to the left child
        self.right = right  # pointer to the right child


class Solution:
    def findInorderSuccessor(self, root: Node, x: Node) -> Node:
        successor = None
        while root:
            if root.data <= x.data:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor
