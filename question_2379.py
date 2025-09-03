class Solution(object):
    def minimumRecolors(self, blocks, k):
        
        min_white = blocks[:k].count("W")
        re_color = min_white

        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                min_white += 1
            if blocks[i-k] == "W":
                min_white -= 1
            re_color = min(min_white, re_color)
        return re_color

