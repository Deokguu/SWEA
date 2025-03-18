'''
4*4 N-Queen 문제
(y,x) 좌표에 queen을 놓은 적이 있다는 걸 기록하며 가야함
visited 기록 방법
    1. 이차원 배열
    2. 일차원 배열로 효율적으로 하는 방법
level: N개의 행에 모두 놓았다.
branch: N개의 열이 후보가 된다
'''
def check(row, col):
    # 1 같은 열에 놓은 적이 있는가
    for i in range(row):
        if visited[row][col]:
            return False
    # 2 왼쪽 대각선에 놓은 적이 있는가
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return False
        i -= 1
        j -= 1

    # 3 오른쪽 대각선에 놓은 적이 있는가
    i, j = row -1, col + 1
    while i >= 0 and j <= N:
        if visited:
            return False
        i -= 1
        j += 1
    return True

def dfs(row):
    global answer
    if row == N:
        answer += 1
        return

    # 후보군: N개의 열
    for col in range(N):
        #가지치기: 유망하지 않은 케이스는 확인하지 않겠다!
        #기존에 같은 열이나 대각선에 놓았다면 못 놓는다!
        if check(row, col):
            continue
        visited[row][col] = 1
        dfs(row + 1)
        visited[row][col] = 0



N = 4
visited = [[0] * N for _ in range(N)]
answer = 0 # 가능한 정답 수

dfs(0)
