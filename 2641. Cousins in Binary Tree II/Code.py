"""
Intuition: 
Cousin nodes are nodes with the same depth but different parent.

Therefore, we need to capture info associated with nodes in the 
same depth. From experience, when it comes to 
dealing with nodes with same depth, BFS traversal 
is the most ideal method. Hence, we apply this.

Given a children, we need to think of a quantity 
that allows us to capture the information of other children with 
different parents in the same depth (i.e cousin info). Moreover, 
BFS traversal restricts movement to a particular children. 
In other words, if you are exploring the children 
of parent A, we can only access the information of parent A's children.
Hence, the quantity must be known to all nodes
in the layer so we only need to make use of children's
information to know the cousin's information.  

A desirable quantity would be the total value of all nodes in a
layer. Reason is that the sum captures all information of the node
in a single layer, and if we want to exclude the value of the
current children we are exploring, we simply need to subtract it.

For e.g
Let's suppose we have children:
A, B, C, D, E, F, G, H

Suppos A and B have the same parent
Sum of all nodes = A + B + C + D + E + F + G + H
Sum of A and B cousins 
= C + D + E + F + G + H
= Sum of all nodes - A - B

Hence we need to first store the total sum of each layer. Then
when we encounter a parent, we can modify the parent's children's
values by substracting the sum of the children's total value from
the total sum of the layer they are in.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #1st iteration: Capture sum of all nodes in a layer

        layer_sum = {} #Stores sum of all nodes in a layer
        deq = deque([(root, 0)]) #A queue for BFS to work. Deque is efficient 
        curr_total = 0 #Current sum of the nodes in a layer
        curr_lvl = -1 #Current layer of the nodes we are exploring

        while deq:
            node, lvl = deq.popleft()
            
            #If at a new layer, update the layer_sum dictionary
            if lvl != curr_lvl:
                layer_sum[curr_lvl] = curr_total
                curr_total = 0
                curr_lvl = lvl

            curr_total += node.val
            if node.left:
                deq.append((node.left, lvl + 1))
            if node.right:
                deq.append((node.right, lvl + 1))

        #This is needed to update the last layer's sum
        #As once we explore all leaves, there are no new
        #layers to explore    
        layer_sum[curr_lvl] = curr_total
        
        deq = deque([(root, 0)])

        #2nd iteration: Modify the child of the parebt given the child's layer
        while deq:
            node, lvl = deq.popleft()
            
            #Note that since only the parent knows
            #all the detail of its children, and the children
            #have no information about their siblings (Same
            #parent nodes), modification must be done via the parent
            #Hence we need to consider lvl + 1
            if lvl + 1 in layer_sum:
                layer = layer_sum[lvl + 1]
                if node.left:
                    if node.right:
                        node.left.val, node.right.val = layer - node.left.val - node.right.val, layer - node.left.val - node.right.val
                        deq.append((node.left, lvl + 1))
                        deq.append((node.right, lvl + 1))
                    else:
                        node.left.val = layer - node.left.val
                        deq.append((node.left, lvl + 1))
                else:
                    if node.right:
                        node.right.val = layer - node.right.val
                        deq.append((node.right, lvl + 1))
        root.val = 0
        return root
        