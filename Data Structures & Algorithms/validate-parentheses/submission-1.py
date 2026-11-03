class Solution:
    def isValid(self, s: str) -> bool:
        corr_bracket = {
            '(': ')',
            '{': '}',
            '[' : ']'
        }
        stack = []
        for bracket in s:
            if bracket in corr_bracket:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                top_open = stack.pop()
                if corr_bracket[top_open] != bracket:
                    return False
        return len(stack) == 0 