class Solution(object):
    def lengthOfLastWord(self, s):
        remove = s.rstrip()
        count = 0
        i = len(remove)-1
        while i >= 0 and s[i] != " ":
            count += 1
            i = i-1
        return count