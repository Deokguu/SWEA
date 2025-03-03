def balloon(arr, N, M):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    max_v = 0
    for row in range(N):
        for col in range(M):
            A = arr[row][col]
            total = arr[row][col]

            for d in range(4):
                for far in range(1, A+1):
                    newR = row + dr[d] * far
                    newC = col + dc[d] * far

                    if 0<=newR<N and 0<=newC<M:
                        total += arr[newR][newC]
            if max_v < total:
                max_v = total
    return max_v



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {balloon(arr, N, M)}')

'''
newC의 범위 체크 오류

현재 if 0<=newR<N and 0<=newC<N:로 검사를 하고 있음.
하지만 N x M 행렬에서 newC의 유효 범위는 0 <= newC < M이어야 함.
즉, newC<N이 아니라 newC<M으로 수정해야 함.
'''