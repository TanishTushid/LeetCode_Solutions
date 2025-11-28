# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        # is Empty
        if not nums:
            return None 
        #mid 
        mid = len(nums) // 2
        #root 
        root = TreeNode(nums[mid])
        #left subtree
        root.left = self.sortedArrayToBST(nums[:mid])
        #right subtree
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root 

        
