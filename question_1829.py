class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        n =  len(nums)
        res = []
        max_value = (1 << maximumBit ) -1
        xor_value = 0

        for num in nums:
            xor_value ^= num
        for i in range(n):
            res.append(xor_value ^ max_value)
            xor_value ^= nums[ -1 - i]
        return res
