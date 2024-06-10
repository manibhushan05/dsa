'''

Given the root of a binary search tree (BST) and a tree node x, find the inorder predecessor of x in the BST. An inorder predecessor of a tree node is the previous node in the inorder traversal of the tree.

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
Output: Node 8

Input: Node 12
Output: Node 10

• If the node does not lie in the BST, return the previous greater node (if any) present in the BST.

Input: Node 18
Output: Node 16

• If the node does not lie in the BST and the previous greater node also does not exist, the solution should return None.

Input: Node 8
Output: None

'''


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data  # data field
        self.left = left  # pointer to the left child
        self.right = right  # pointer to the right child


class Solution:
    def findInorderPredecessor(self, root: Node, x: Node) -> Node:
        predecessor = None
        while root:
            if root.data >= x.data:
                root = root.left
            else:
                predecessor = root
                root = root.right
        return predecessor
