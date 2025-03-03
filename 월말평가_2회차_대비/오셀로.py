dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

def change(arr, i, j, color):
    arr[i][j] = color
    for d in range(8):
        newR, newC = i + dr[d], j + dc[d]
        temp = []
        while 0<=newR<N and 0<=newC<N:
            if arr[newR][newC] == 0:
                break
            if arr[newR][newC] == color:
                for ci, cj in temp:
                    arr[ci][cj] = color
                break
            temp.append([newR, newC])
            newR += dr[d]
            newC += dc[d]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]

    mid = N // 2
    board[mid-1][mid-1], board[mid][mid] = 2, 2
    board[mid][mid-1], board[mid-1][mid] = 1, 1

    for _ in range(M):
        i, j, color = map(int, input().split())
        i -= 1
        j -= 1
        change(board, i, j, color)

    white_cnt = 0
    black_cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black_cnt += 1
            elif board[i][j] == 2:
                white_cnt += 1
    print(f'#{tc} {black_cnt} {white_cnt}')

'''
돌을 실제로 놓는 작업 빼먹음
뒤집는 조건이 올바르지 않음 언제 break를 하는지 잘 생각해봐야함
중간에 빈칸이 있을 때, 같은 색깔이 있을 때, 범위를 벗어날 때
'''