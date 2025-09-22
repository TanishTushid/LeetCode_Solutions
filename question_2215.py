class Solution(object):
    def findDifference(self, nums1, nums2):
        nums1, nums2 = sorted(set(nums1)), sorted(set(nums2))
        i,j = 0,0
        result1, result2 = [],[]
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result1.append(nums1[i])
                i += 1
            elif nums2[j] < nums1[i]:
                result2.append(nums2[j])
                j += 1
            else:
                i += 1
                j += 1
        while i < len(nums1):
            result1.append(nums1[i])
            i += 1
        while j < len(nums2):
            result2.append(nums2[j])
            j += 1
        return [result1, result2]

        