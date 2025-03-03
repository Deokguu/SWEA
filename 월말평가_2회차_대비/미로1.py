dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def start(arr):
    for row in range(16):
        for col in range(16):
            if arr[row][col] == 2:
                return row, col
def dfs(arr, si, sj):
    stack = []
    visited = [[False] * 16 for _ in range(16)]
    stack.append([si, sj])
    visited[si][sj] = True

    while stack:
        ti, tj = stack.pop()
        if arr[ti][tj] == 3:
            return 1
        for d in range(4):
            ni = ti + dr[d]
            nj = tj + dc[d]

            if 0<=ni<16 and 0<=nj<16:
                if arr[ni][nj] != 1 and not visited[ni][nj]:
                    stack.append([ni, nj])
                    visited[ni][nj] = True
    return 0
T = 10

for tc in range(1, T+1):
    tc_num = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    si, sj = start(arr)
    print(f'#{tc_num} {dfs(arr, si, sj)}')

'''
입력값!!!!!!!!!!!!!! 어떻게 받는지 주의
tc 번호를 입력받는 건 아닌지 확인 요망
visited만 쓰지말고 visited[ni][nj]처럼 인덱스도 꼭 넣어주기
'''