def solve():
    s = input()
    opening = set()
    closing = set()
    if s[0] == s[-1]:
        return False
    opening.add(s[0])
    closing.add(s[-1])

    # treat the remaining one to be opening
    stack = []
    for char in s:
        if char in opening:
            stack.append("(")
        elif char in closing:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
        else:
            stack.append('(')
    if not stack:
        return True
    
    stack = []
    for char in s:
        if char in opening:
            stack.append("(")
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
    
    return not stack

t = int(input())
for _ in range(t):
    if solve():
        print("YES")
    else:
        print("NO")