class Solution(object):
    def longestContinuousSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 1
        running = 1
        for i in range(1,len(s)):
            if ord(s[i]) == ord(s[i-1]) +1:
                running += 1
                ans = max(ans, running)
            else:
                running = 1
        return ans