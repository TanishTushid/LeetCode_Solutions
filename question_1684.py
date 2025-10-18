class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allow_set =  set(allowed)
        count = 0
        for word in words:
            consistent = True
            for ch in word:
                if ch not in allow_set:
                    consistent = False
                    break
            if consistent:
                count += 1
        return count
        