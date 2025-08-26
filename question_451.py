class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        frequency = Counter(s)
        sorted_string = sorted(frequency.items(), key= lambda X:X[1], reverse = True)
        result = ""
        for char, count in sorted_string:
            result += char * count 
        return result