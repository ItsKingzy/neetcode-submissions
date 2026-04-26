class Solution:
    def isValid(self, s: str) -> bool:
        charArr = list(s)
        stack = []

        if charArr == []:
            return False

        for i, char in enumerate(charArr):
            if char in ")]}":
                if stack == []:
                    return False
                elif char == ")":
                    if stack[-1] != "(":
                        return False
                elif char == "]":
                    if stack[-1] != "[":
                        return False
                elif char == "}":
                    if stack[-1] != "{":
                        return False

            if char in "([{":
                stack.append(char)
            else:
                if char == ")":
                    if stack[-1] == "(":
                        stack.pop()

                elif char == "]":
                    if stack[-1] == "[":
                        stack.pop()

                elif char == "}":
                    if stack[-1] == "{":
                        stack.pop()

        if stack == []:
            return True
        else:
            return False

