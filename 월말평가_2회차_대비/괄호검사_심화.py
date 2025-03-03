def test(words):
    stack = []
    for letter in words:
        if letter in '({[<':
            stack.append(letter)
        elif letter in ')}]>':
            if not stack:
                return 0
            if stack:
                t = stack.pop()
                if t == '(' and letter != ')':
                    return 0
                elif t == '{' and letter != '}':
                    return 0
                elif t == '[' and letter != ']':
                    return 0
                elif t == '<' and letter != '>':
                    return 0
    if not stack:
        return 1
    else:
        return 0

T = 10

for tc in range(1, T+1):
    length = int(input())
    arr = list(input())
    print(f'#{tc} {test(arr)}')


'''
스택이 비어있을 때 pop을 호출하면 오류 발생할 수 있으니 비어있을 때 return 0
'''

