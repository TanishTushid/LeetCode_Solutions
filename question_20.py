class Solution(object):
    def isValid(self,s):
        valid_parentheses = {
            "]":"[", "}":"{", ")":"("
        }
        stack = []

        for ch in s:
            if ch in valid_parentheses:
                top_element = stack.pop() if stack else "#"
                if valid_parentheses[ch] != top_element:
                    return False
                else:
                    stack.append(ch)
            return not stack