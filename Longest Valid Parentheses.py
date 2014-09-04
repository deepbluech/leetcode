def longestValidParentheses(s):
    n = len(s)
    max = 0
    stack = []
    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        else:
            if len(stack) > 0 and s[stack[-1]] == '(':
                stack.pop()
                if len(stack) > 0:
                    cur_len = i - stack[-1]
                else:
                    cur_len = i + 1
                if cur_len > max:
                    max = cur_len
            else:
                stack.append(i)
    return max

print longestValidParentheses("()((()")