T = int(input())

for tc in range(1, T + 1):
    arr = list(input())  # 문자열을 리스트로 변환
    STACK = []

    for x in arr:
        if STACK and STACK[-1] == x:
            STACK.pop()  # 중복된 문자 제거
        else:
            STACK.append(x)

    print(f'#{tc} {len(STACK)}')
