T = 10

def solve():
    N, arr = list(input().split())
    stack = []
    for i in arr:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return stack


for tc in range(1, T+1):
    print(f'#{tc} ', *solve(), sep = '')