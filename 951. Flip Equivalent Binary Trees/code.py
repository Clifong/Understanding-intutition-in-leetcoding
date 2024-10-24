'''
Intutition:

To first solve, we need to first understand the impact of flipping
on a certain node. 

Observing the sample cases, notice an important fact:

Flipping does not alter parent node. In fact, flipping allows you
to switch position of the child for the same parent. For e.g

if the tree is originally,
   X
  / \   
  Y Z

Flipping allows us to form
  X
 / \ 
 Z Y

 Z and Y swap positions!

Conclusion: To check if flipping is possible, we only needt 
to care about the parent of a node.

Therefore, we can either do a DFS or BFS traversal to store the 
parent of any node in each tree inside a dictionary

Then we simply need to check if for a node, both dictionary entries
contain the same value (i.e same parent).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        r1_node = {} #Store all node-parent info in tree 1
        r2_node = {} #Store all node-parent info in tree 2
        
        
        # Edge cases when some of the root is None
        if root1:
            r1_q = deque([(root1, None)])
            r1_node[root1.val] = None
        else:
            r1_q = deque([])
        if root2:
            r2_q = deque([(root2, None)])
            r2_node[root2.val] = None
        else:
            r2_q = deque([])

        if root1 and root2 and root1.val != root2.val:
            return False

        #BFS traversal to find the node-parent pairing
        #for each tree
        while r1_q and r2_q:
            n1, parent1 = r1_q.popleft()
            n2, parent2 = r2_q.popleft()

            if n1.val not in r1_node and parent1 != None:
                r1_node[n1.val] = parent1.val
            if n2.val not in r2_node and parent2 != None:
                r2_node[n2.val] = parent2.val
            
            if n1.left:
                r1_q.append((n1.left, n1))
            if n1.right:
                r1_q.append((n1.right, n1))
            if n2.left:
                r2_q.append((n2.left, n2))
            if n2.right:
                r2_q.append((n2.right, n2))

        # Trees aren't even the same size! Fail
        if len(r1_q) != len(r2_q):
            return False
        
        # Check if for a node, the parent is the same
        for i in range(1, 101):
            if i not in r1_node:
                return True
            if r1_node[i] != r2_node[i]:
                return False
         # type: ignore