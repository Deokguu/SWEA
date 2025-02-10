T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    #우, 하, 좌, 상

    delta = [(0,1), (1,0), (0,-1), (-1,0)]
    d = 0
    row = col = 0
    # value = 1

    for i in range(1, N*N +1):
        arr[row][col] = i
        newR = row + delta[d][0]
        newC = col + delta[d][1]
        if newR < 0 or newR >= N or newC < 0 or newC >=N or arr[newR][newC] != 0:#newR, newC 범위를 벗어났거나 이미 데이터가 있으면 방향전환
            d = (d+1) % 4
            #d = d+1
            #if d==4:
            #   d = 0
        row += delta[d][0]
        col += delta[d][1]
    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])
        # print(' '.join(map(str, arr[i])))
