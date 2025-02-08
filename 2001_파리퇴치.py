T = int(input())

for tc in range(1, T+1):
    N, M = (map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    max_flies = 0
    
    for i in range(N):
        for j in range(N):
            s = 0
            for p in range(M):
                for q in range(M):
                    ni, nj = i + p, j + q
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]
                    
            if max_flies < s:
                max_flies = s
    print(f'#{tc} {max_flies}')               
