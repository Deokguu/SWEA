T = int(input())

for tc in range(1, T+1):
    arr = list(input())
    # print(arr)
    # top = -1
    # SIZE = len(arr)
    # STACK = [0] * SIZE
    # answer = 1
    # # print(arr)
    # for x in arr:
    #     if x in '({':  # 여는 괄호 push, if x in '({[<':
    #         top += 1
    #         STACK[top] = x
    #     elif x in ')}':  # 공백 제거할 겸 elif 씀
    #         if top == -1:  # 스택이 비어있으면
    #             answer = 0
    #             break  # for x
    #         else:
    #             top -= 1
    STACK = []
    for c in arr:
        if c == '(':
            STACK.append(c)
        elif c in ')}':
            if not STACK:
                answer = 0
                break
            temp = STACK.pop()
            if temp != :
                answer = 0

    if STACK:
        answer = 0


        # print(STACK)
    # if top > -1:
    #     answer = 0
    print(f'#{tc} {answer}')

