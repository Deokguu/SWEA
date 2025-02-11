def isPali(s):
    for i in range(N//2):
        if s[i] != s[N-1-i]:
            return False
    return True

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(8)]

    cnt = 0
    for row in range(8):
        for start in range(8 - N + 1):  # 예시 하나 잡고 해보기
            if isPali(arr[row][start: start + N]):
                cnt += 1
    # 세로로 갈 땐 슬라이싱을 못 씀.
    for col in range(8):
        for start in range(8 - N + 1):
            s = ''
            for row in range(start, start + N):  # 슬라이싱 대신 씀
                s += arr[row][col]
            if isPali(s):
                cnt += 1

    print(f'#{tc} {cnt}')


