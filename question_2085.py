from collections import Counter
class Solution(object):
    def countWords(self, words1, words2):
        count_1 = Counter(words1)
        count_2 = Counter(words2)
        result = 0
        for w in count_1:
            if count_1[w] == 1 and count_2.get(w,0) == 1:
                result += 1
        return result

        