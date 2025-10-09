class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end) //2
            if nums[mid] > mid:
                end = mid - 1
            else:
                start = mid + 1 
        return start
            
        