T = int(input())

for tc in range(1, T+1):
    arr = input()
    stack = []
    ans = 1
    
    for c in arr:
        if c in '({':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] == '{':
                ans = 0
                break

            elif stack[-1] == '(':
                stack.pop()

        elif c == '}':
            if not stack or stack[-1] == '(':
                ans = 0
                break

            elif stack[-1] == '{':
                stack.pop()

    if stack:
        ans = 0            
    
    print(f'#{tc} {ans}')


            


