T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr_puzzle = [list(map(int, input().split())) for _ in range(N)]
    
    cnt = 0

    # print(arr_puzzle)
    #행부터 순회
    for i in range(N):
        for j in range(N-K+1):
            if sum(arr_puzzle[i][j:j+K]) == K:
                if (j == 0 or arr_puzzle[i][j-1] == 0) and (j + K == N or arr_puzzle[i][j+K] == 0):
                    cnt += 1

    #열 순회
    
    for j in range(N):
        for i in range(N - K + 1):
            col_total = 0
            for p in range(i, i+K):
                col_total += arr_puzzle[p][j]
            if col_total == K:
                if (i == 0 or arr_puzzle[i-1][j] == 0) and (i + K == N or arr_puzzle[i + K][j] == 0):
                    cnt += 1

    print(f'#{tc} {cnt}')



