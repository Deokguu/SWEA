T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = input()
    stack = []
    ans = 1

    for s in arr:
        if s in '({<[':
            stack.append(s)
        elif s == ')':
            if not stack:
                ans = 0
                break
            elif stack[-1] == '(':
                stack.pop()
            elif stack[-1] in '<{[':
                ans = 0
                break
        elif s == '}':
            if not stack:
                ans = 0
                break
            elif stack[-1] == '{':
                stack.pop()
            elif stack[-1] in '[(<':
                ans = 0
                break
        elif s == '>':
            if not stack:
                ans = 0
                break
            elif stack[-1] == '<':
                stack.pop()
            elif stack[-1] in '{[(':
                ans = 0
                break
        elif s == ']':
            if not stack:
                ans = 0
                break
            elif stack[-1] == '[':
                stack.pop()
            elif stack[-1] in '<{(':
                ans = 0
                break
    if stack:
        ans = 0

    print(f'#{tc} {ans}')
