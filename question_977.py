class Solution(object):
    def sortedSquares(self, nums):
        # brute force
        """
        result = []
        for i in nums:
            result.append(i*i)
        result.sort()
        return result
        """
        #optimize code
        n = len(nums)
        result = [0]*n
        left, right, pos = 0, n-1, n-1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] * nums[left]
                left += 1
            else:
                result[pos] = nums[right] * nums[right]
                right -= 1
            pos -= 1
        return result

        
