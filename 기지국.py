dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def solve(arr, si, sj):
    if arr[si][sj] == 'A':
        length = 1
    elif arr[si][sj] == 'B':
        length = 2
    elif arr[si][sj] == 'C':
        length = 3

    for d in range(4):
        for far in range(1, length+1):
            ni, nj = si + far*dr[d], sj + far*dc[d]

            if 0<=ni<n and 0<=nj<n and arr[ni][nj] == 'H':
                arr[ni][nj] = 'Q'
    
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    broad = [list(input()) for _ in range(n)]
    # print(broad)
    for row in range(n):
        for col in range(n):
            if broad[row][col] in 'ABC':
                solve(broad, row, col)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if broad[i][j] == 'H':
                cnt += 1
    print(f'#{tc} {cnt}')
