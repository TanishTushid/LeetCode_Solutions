
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        self.prev = None
        self.count = 0
        self.maxcount = 0
        self.result = []

        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            if self.prev == node.val:
                self.count += 1
            else:
                self.count = 1
            if self.count > self.maxcount:
                self.maxcount = self.count
                self.result = [node.val]
            elif self.count == self.maxcount:
                self.result.append(node.val)
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        return self.result
