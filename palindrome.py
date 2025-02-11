def isPali(s):
    for i in range(M // 2):
        if s[i] != s[M-1-i]:
            return False
    return True

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    answer = ''

    for row in range(N):
        # 한 줄에 대해서
        for start in range(N - M + 1):  # 예시 하나 잡고 해보기
            if isPali(arr[row][start: start + M]):
                answer = arr[row][start: start + M]
    # 세로로 갈 땐 슬라이싱을 못 씀.
    for col in range(N):
        for start in range(N - M + 1):
            s = '' #빈 문자열
            for row in range(start, start + M):  # 세로문자열 뽑아오기
                s += arr[row][col]
            if isPali(s):
                answer = s
    answer = ''.join(answer)
    print(f'#{tc} {answer}')

