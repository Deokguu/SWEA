'''
def dfs(row, col, isCut, curV):
    visited[row][col] = True
    for dx, dy in []:
        newR =
        newC =
        if 방문안한경우:
            if 갈 수 있는경우:
                dfs(newR, newC, isCut, arr[newR][newC])
            elif 깎으면 갈 수 있는지 and isCut == 0:
                arr[newR][newC] = 깎고 난 이후의 값
                dfs(newR, newC, 1, 깎고 난 이후의 값)
                arr[newR][newC] = 원복
    visited[row][col] = False
'''
def find_max(arr):
    max_v = 0
    for lst in range(N):
        if max_v < max(lst):
            max_v = max(lst)
    for row in range(N):
        for col in range(N):
            if arr[row][col] == max_v
    return max_v

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if arr[row][col]
    find_max(arr)