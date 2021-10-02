# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxima = float("-inf")
        self.score = 0
        self.check_node(root, maxima)
        return self.score


    def check_node(self, node, maxima):
        if node.val >= maxima:
            self.score= self.score+1
        passage = max(maxima, node.val)
        if node.left != None:
            self.check_node(node.left,passage)
        if node.right != None:
            self.check_node (node.right,passage)
