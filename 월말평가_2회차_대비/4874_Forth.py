def calculate(arr):
    stack = []
    for i in arr:
        if i == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'
        elif i.isdigit():
            stack.append(i)
        elif i in '+-*/':
            if len(stack) < 2:
                return 'error'
            else:
                    
                t2 = int(stack.pop())
                t1 = int(stack.pop())
                if i == '+':
                    stack.append(t1+t2)
                elif i == '/':
                    if t2 == 0:
                        return 'error'
                    stack.append(t1/t2)
                elif i == '-':
                    stack.append(t1-t2)
                elif i == '*':
                    stack.append(t1*t2)
        else:
            return 'error'

    return 'error'

T = int(input())

for tc in range(1, T+1):
    arr = list(input().split())
    print(f'#{tc} {calculate(arr)}')
