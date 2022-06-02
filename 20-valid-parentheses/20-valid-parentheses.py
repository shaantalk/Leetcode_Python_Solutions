class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        opens = ["(","{","["]
        
        for char in s:
            if char in opens:
                stack.append(char)
            else:
                if not stack:
                    return False
                poppedChar = stack.pop()
                if poppedChar != closeToOpen[char]:
                    return False
        return False if stack else True