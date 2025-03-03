def test(words):
    stack = []

    for letter in words:
        if letter in "({": # ({이면 스택에 추가
            stack.append(letter)
        elif letter in ")}": # 스택이 비어있지 않고 )}이면 스택 최상단에 있는 거 꺼내서 검사
            if not stack:
                return 0
            else:
                t = stack.pop()
                if t == '(':
                    if letter != ')':
                        return 0
                if t == '{':
                    if letter != '}':
                        return 0
    if not stack:
        return 1
    else:
        return 0
                

T = int(input())

for tc in range(1, T+1):
    arr = list(input())

    print(f'#{tc} {test(arr)}')


'''
pop할 때 꼭 스택 비어있지 않은지 검사
while문이면 while stack: / for문이면 pop 동작 하기 전에 조건 걸어주기
'''
